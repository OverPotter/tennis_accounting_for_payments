from typing import Sequence, Type

from sqlalchemy import Row, and_, func, select, text
from sqlalchemy.orm import joinedload

from src.database.models.models import (
    ClientModel,
    NumberOfTennisTrainingAvailableModel,
    PaymentModel,
    VisitModel,
)
from src.database.repositories.absctract_repository import AbstractRepository
from src.utils.check_entity_exists import (
    check_entity_does_not_exist_by_name,
    check_entity_exists_by_name,
)


class ClientRepository(AbstractRepository[ClientModel]):
    _model = ClientModel

    async def check_client_does_not_exist_by_name(self, name: str) -> None:
        client_data = await self.get(name=name)
        check_entity_does_not_exist_by_name(
            data=client_data, model=self._model, value=name
        )

    async def get_or_raise_by_name(self, name: str) -> _model:
        client_data = await self.get(name=name)
        check_entity_exists_by_name(
            data=client_data, model=self._model, value=name
        )

        return client_data

    async def get_user_with_number_of_tennis_training_available(
        self, client_name: str
    ) -> _model:
        query = (
            select(self._model)
            .options(
                joinedload(self._model.number_of_trainings_available).options(
                    joinedload(NumberOfTennisTrainingAvailableModel.coach)
                )
            )
            .filter_by(name=client_name)
        )

        result = await self._session.execute(query)
        client_data = result.unique().scalar_one_or_none()

        check_entity_exists_by_name(
            data=client_data, model=self._model, value=client_name
        )

        return client_data

    async def get_client_visits_in_3_months(
        self, client_name: str
    ) -> Sequence[Row[tuple[_model, VisitModel]]]:
        return await self._get_client_data_in_last_3_months(
            related_model=VisitModel,
            client_name=client_name,
            date_field=VisitModel.visit_datetime.key,
        )

    async def get_client_payments_in_3_months(
        self, client_name: str
    ) -> Sequence[Row[tuple[_model, PaymentModel]]]:
        return await self._get_client_data_in_last_3_months(
            related_model=PaymentModel,
            client_name=client_name,
            date_field=PaymentModel.payment_date.key,
        )

    async def _get_client_data_in_last_3_months(
        self,
        related_model: Type[PaymentModel | VisitModel],
        client_name: str,
        date_field: str,
    ) -> Sequence[Row[tuple[_model, PaymentModel | VisitModel]]]:

        query = (
            select(self._model, related_model)
            .join(related_model, self._model.id == related_model.client_id)
            .where(
                and_(
                    getattr(related_model, date_field)
                    >= func.now() - text("INTERVAL '3 MONTH'"),
                    self._model.name == client_name,
                )
            )
            .options(joinedload(related_model.coach))
            .order_by(getattr(related_model, date_field).desc())
        )

        result = await self._session.execute(query)
        client_data = result.fetchall()

        check_entity_exists_by_name(
            data=client_data, model=self._model, value=client_name
        )

        return client_data
