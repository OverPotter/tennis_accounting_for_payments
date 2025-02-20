from typing import Sequence, Type

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

    async def _get_client_data_in_last_3_months(
        self,
        related_model: Type[PaymentModel | VisitModel],
        client_name: str,
        date_field: str,
    ) -> Sequence[Row[tuple[ClientModel, PaymentModel | VisitModel]]]:

        query = (
            select(ClientModel, related_model)
            .join(related_model, ClientModel.id == related_model.client_id)
            .where(
                and_(
                    getattr(related_model, date_field)
                    >= func.now() - text("INTERVAL '3 MONTH'"),
                    ClientModel.name == client_name,
                )
            )
            .order_by(getattr(related_model, date_field).desc())
        )

        result = await self._session.execute(query)
        return result.fetchall()

    async def get_client_visits_in_3_months(
        self, client_name: str
    ) -> Sequence[Row[tuple[ClientModel, VisitModel]]]:
        return await self._get_client_data_in_last_3_months(
            VisitModel, client_name, "visit_datetime"
        )

    async def get_client_payments_in_3_months(
        self, client_name: str
    ) -> Sequence[Row[tuple[ClientModel, PaymentModel]]]:
        return await self._get_client_data_in_last_3_months(
            PaymentModel, client_name, "payment_date"
        )
