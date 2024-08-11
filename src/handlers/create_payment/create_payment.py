from datetime import datetime
from typing import Optional

from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)


class CreatePaymentCommandHandler:
    def __init__(self, service: RepositoryPaymentService):
        self._service = service

    async def _validate_datetime(
        self, client_name: str, amount: float, payment_date_str: str
    ) -> Optional[bool]:
        try:
            datetime.strptime(payment_date_str, "%Y.%m.%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")

        return await self._service.create_payment(
            client_name, amount, payment_date_str
        )
