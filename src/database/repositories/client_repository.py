from typing import Any, Sequence

from sqlalchemy import Row, select, text
from sqlalchemy.orm import joinedload

from src.database.models.models import ClientModel, PaymentModel
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
    ) -> _model | None:
        three_months_ago = (datetime.now() - timedelta(days=90)).date()

        query = (
            select(ClientModel)
            .options(joinedload(ClientModel.payments))
            .filter_by(name=client_name)
            .join(ClientModel.payments)
            .filter(PaymentModel.payment_date >= three_months_ago)
        )

        result = await self._session.execute(query)
        client = result.unique().scalar_one_or_none()

        if client:
            client.payments = [
                payment
                for payment in client.payments
                if payment.payment_date >= three_months_ago
            ]
            return client
        else:
            return None
