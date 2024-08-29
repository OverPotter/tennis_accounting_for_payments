from typing import Any, Sequence

from sqlalchemy import Row, select, text
from sqlalchemy.orm import joinedload

from src.database.models.models import ClientModel
from src.database.repositories.absctract_repository import AbstractRepository


class ClientRepository(AbstractRepository[ClientModel]):
    _model = ClientModel

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

    async def get_user_monthly_visits(
        self, client_name: str
    ) -> Sequence[Row[tuple[Any, ...]]]:
        query = text(
            """
            select * from clients
            join visits on clients.id = visits.client_id
            where visits.visit_datetime >= NOW() - INTERVAL 3 MONTH AND clients.name = :client_name
            order by visits.visit_datetime DESC;
            """
        )

        result = await self._session.execute(
            query, {"client_name": client_name}
        )
        return result.fetchall()

    async def get_user_monthly_payments(
        self, client_name: str
    ) -> Sequence[Row[tuple[Any, ...]]]:
        query = text(
            """
            select payments.client_id, payments.payment_date, payments.amount
            from clients
            join payments on clients.id = payments.client_id
            where payments.payment_date >= NOW() - INTERVAL 3 MONTH 
            AND clients.name = :client_name
            order by payments.payment_date DESC;
            """
        )

        result = await self._session.execute(
            query, {"client_name": client_name}
        )
        return result.fetchall()
