from datetime import datetime
from typing import Sequence


from src.database.models.models import PaymentModel
from src.database.repositories.absctract_repository import AbstractRepository


class PaymentRepository(AbstractRepository[PaymentModel]):
    _model = PaymentModel

    async def get_all_paid_client_training_up_to_current_month(
        self, client_id: int, until_what_month: datetime.date
    ) -> Sequence[PaymentModel]:
        return await self.get_all_by_client_up_to_date(
            client_id=client_id,
            date_field="payment_date",
            until_what_month=until_what_month,
        )

    async def get_monthly_client_paid_training_visits(
        self,
        client_id: int,
        first_day_of_current_month: datetime.date,
        last_day_of_current_month: datetime.date,
    ) -> Sequence[PaymentModel]:
        return await self.get_monthly_client_entries(
            client_id=client_id,
            date_field="payment_date",
            first_day_of_current_month=first_day_of_current_month,
            last_day_of_current_month=last_day_of_current_month,
        )
