from datetime import datetime
from typing import Sequence

from sqlalchemy import desc, select

from src.database.models.models import PaymentModel
from src.database.repositories.absctract_repository import AbstractRepository


class PaymentRepository(AbstractRepository[PaymentModel]):
    _model = PaymentModel

    async def get_all_paid_client_training_up_to_current_month(
        self, client_id: int, until_what_month: datetime.date
    ) -> Sequence[PaymentModel]:
        query = (
            select(PaymentModel)
            .filter(
                PaymentModel.client_id == client_id,
                PaymentModel.payment_date < until_what_month,
            )
            .order_by(desc(PaymentModel.payment_date))
        )

        result = await self._session.execute(query)
        return result.scalars().fetchall()

    async def get_monthly_client_paid_training_visits(
        self,
        client_id: int,
        first_day_of_current_month: datetime.date,
        last_day_of_current_month: datetime.date,
    ) -> Sequence[PaymentModel]:
        query = (
            select(PaymentModel)
            .filter(
                PaymentModel.client_id == client_id,
                PaymentModel.payment_date >= first_day_of_current_month,
                PaymentModel.payment_date <= last_day_of_current_month,
            )
            .order_by(desc(PaymentModel.payment_date))
        )

        result = await self._session.execute(query)
        return result.scalars().fetchall()
