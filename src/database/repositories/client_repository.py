from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.database.models.models import ClientModel, PaymentModel, VisitModel
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

    async def get_user_monthly_visits(self, client_name: str) -> _model | None:
        three_months_ago = datetime.now() - timedelta(days=90)

        query = (
            select(ClientModel)
            .options(joinedload(ClientModel.visits))
            .filter_by(name=client_name)
            .join(ClientModel.visits)
            .filter(VisitModel.visit_datetime >= three_months_ago)
        )

        result = await self._session.execute(query)
        client = result.unique().scalar_one_or_none()

        if client:
            client.visits = [
                visit
                for visit in client.visits
                if visit.visit_datetime >= three_months_ago
            ]
            return client
        else:
            return None

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
