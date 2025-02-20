from typing import Sequence

from sqlalchemy import Row, and_, func, select, text
from sqlalchemy.orm import joinedload

from src.database.models.models import ClientModel, PaymentModel, VisitModel
from src.database.repositories.absctract_repository import AbstractRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException


class ClientRepository(AbstractRepository[ClientModel]):
    _model = ClientModel

    async def get_or_raise_by_name(self, name: str) -> _model:
        entity = await self.get(name=name)
        if not entity:
            raise EntityDoesntExistException(
                key=self._model.name.key,
                value=name,
                entity_name=self._model.__tablename__,
            )
        return entity

    async def get_user_with_number_of_tennis_training_available(
        self, client_name: str
    ) -> _model | None:
        query = (
            select(ClientModel)
            .options(joinedload(ClientModel.number_of_trainings_available))
            .filter_by(name=client_name)
        )

        result = await self._session.execute(query)
        return result.unique().scalar_one_or_none()

    async def get_client_visits_in_3_months(
        self, client_name: str
    ) -> Sequence[Row[tuple[ClientModel, VisitModel]]]:
        query = (
            select(ClientModel, VisitModel)
            .join(VisitModel, ClientModel.id == VisitModel.client_id)
            .where(
                and_(
                    VisitModel.visit_datetime
                    >= func.now() - text("INTERVAL '3 MONTH'"),
                    ClientModel.name == client_name,
                )
            )
            .order_by(VisitModel.visit_datetime.desc())
        )

        result = await self._session.execute(query)
        return result.fetchall()

    # todo: DRY
    async def get_client_payments_in_3_months(
        self, client_name: str
    ) -> Sequence[Row[tuple[ClientModel, PaymentModel]]]:
        query = (
            select(ClientModel, PaymentModel)
            .join(PaymentModel, ClientModel.id == PaymentModel.client_id)
            .where(
                and_(
                    PaymentModel.payment_date
                    >= func.now() - text("INTERVAL '3 MONTH'"),
                    ClientModel.name == client_name,
                )
            )
            .order_by(PaymentModel.payment_date.desc())
        )

        result = await self._session.execute(query)
        return result.fetchall()
