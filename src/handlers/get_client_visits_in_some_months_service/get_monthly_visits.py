from aiogram import types

from src.decorators.error_handler import error_handler
from src.handlers.base import BaseCommandHandler
from src.services.get_client_visits_in_some_months_service.abc import (
    AbstractGetClientVisitsInSomeMonthsService,
)
from src.utils.create_answer_about_monthly_visits import (
    create_answer_about_monthly_visits,
)
from src.utils.validators.validate_name import validate_full_name


class GetClientVisitsInSomeMonthsCommandHandler(BaseCommandHandler):
    def __init__(
        self,
        get_client_visits_in_some_months_service: AbstractGetClientVisitsInSomeMonthsService,
    ):
        super().__init__()
        self._get_client_visits_in_some_months_service = (
            get_client_visits_in_some_months_service
        )

    @error_handler
    async def handle(self, message: types.Message) -> None:
        client_name = validate_full_name(full_name=message.text)

        if client_name:

            client_with_monthly_visits = await self._get_client_visits_in_some_months_service.get_client_visits_in_3_months(
                client_name=client_name
            )

            if client_with_monthly_visits:
                self._logger.info(f"Client {client_name} has visits.")
                answer_message = create_answer_about_monthly_visits(
                    data=client_with_monthly_visits
                )
                await message.answer(answer_message)
            else:
                self._logger.warning(
                    f"No visits found for client {client_name}."
                )
                await message.answer(
                    "Посещения за текущий месяц не найдены. Сообщите администратору."
                )
