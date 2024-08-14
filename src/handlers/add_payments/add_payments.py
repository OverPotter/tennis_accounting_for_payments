from datetime import datetime

from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)
from src.services.logging_service.logging_service import Logger


class CreatePaymentsCommandHandler:
    def __init__(
        self,
        create_payment_service: RepositoryPaymentService,
        logger: Logger,
    ):
        self._create_payment_service = create_payment_service
        self._logger = logger

    def _validate_datetime(self, payment_date: str) -> None:
        try:
            datetime.strptime(payment_date, "%Y.%m.%d").date()
        except ValueError:
            self._logger.error("Invalid date format. Expected YYYY.MM.DD.")
