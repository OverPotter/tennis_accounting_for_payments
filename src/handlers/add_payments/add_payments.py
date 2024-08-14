from datetime import datetime

from src.exceptions.user_exception import PaymentExist
from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)
from src.services.logging_service.logging_service import Logger


class AddPaymentsCommandHandler:
    def __init__(
        self,
        create_payment_service: RepositoryPaymentService,
        logger: Logger,
    ):
        self._create_payment_service = create_payment_service
        self._logger = logger

    def _validate_datetime(self, payment_date: str) -> None:
        try:
            datetime.strptime(payment_date, "%d.%m.%Y").date()
        except ValueError:
            self._logger.error("Invalid date format. Expected DD.MM.YYYY.")

    async def handle(
        self, client_name: str, amount: float, payment_date: str
    ) -> bool:

        self._validate_datetime(payment_date)

        try:
            return await self._create_payment_service.create_payment(
                client_name, amount, payment_date
            )
        except PaymentExist as e:
            self._logger.error(f"Failed to create payment: {e}")
            return False
