from datetime import datetime

from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)


class CreatePaymentCommandHandler:
    def __init__(self, create_payment_service: RepositoryPaymentService):
        self._create_payment_service = create_payment_service

    async def _validate_datetime(
        self, client_name: str, amount: float, payment_date: str
    ) -> bool:
        try:
            datetime.strptime(payment_date, "%Y.%m.%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY.MM.DD.")

        return await self._create_payment_service.create_payment(
            client_name, amount, payment_date
        )
