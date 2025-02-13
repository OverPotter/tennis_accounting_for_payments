from aiogram import types

from src.decorators.error_handler import error_handler
from src.handlers.base import BaseCommandHandler
from src.services.get_client_payments_in_some_months_service.abc import (
    AbstractGetClientPaymentsInSomeMonthsService,
)
from src.utils.create_answer_about_monthly_payments import (
    create_answer_about_monthly_payments,
)
from src.utils.validators.validate_client_name import (
    validate_and_extract_client_name,
)


class GetClientPaymentsInSomeMonthsCommandHandler(BaseCommandHandler):
    def __init__(
        self,
        get_client_payments_in_some_months_service: AbstractGetClientPaymentsInSomeMonthsService,
    ):
        super().__init__()
        self._get_client_payments_in_some_months_service = (
            get_client_payments_in_some_months_service
        )

    @error_handler
    async def handle(self, message: types.Message) -> None:
        client_name_parts = message.text.split(" ", 1)

        client_name = validate_and_extract_client_name(parts=client_name_parts)

        if client_name:

            client_with_monthly_payments = await self._get_client_payments_in_some_months_service.get_client_payments_in_3_months(
                client_name=client_name
            )

            if client_with_monthly_payments:
                self._logger.info(f"Client {client_name} has payments.")
                answer_message = create_answer_about_monthly_payments(
                    data=client_with_monthly_payments
                )
                await message.answer(answer_message)
            else:
                self._logger.warning(
                    f"No payments found for client {client_name}."
                )
                await message.answer(
                    "Оплата за текущий месяцы не найдена. Сообщите администратору."
                )
