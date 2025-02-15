from aiogram import types

from src.decorators.error_handler import error_handler
from src.handlers.base import BaseCommandHandler
from src.services.create_client_service.abc import AbstractCreateClientService
from src.utils.validators.validate_name import validate_and_extract_name


class AddClientCommandHandler(BaseCommandHandler):
    def __init__(self, create_client_service: AbstractCreateClientService):
        super().__init__()
        self._create_client_service = create_client_service

    @error_handler
    async def handle(self, message: types.Message) -> None:
        client_name_parts = message.text.split(" ", 1)

        client_name = validate_and_extract_name(parts=client_name_parts)

        if client_name:

            if await self._create_client_service.create_client(
                client_name=client_name
            ):
                self._logger.info(
                    f"The client {client_name} has been successfully created."
                )
                await message.answer("Клиент успешно добавлен.")

            else:
                self._logger.warning(
                    f"The client {client_name} has not been created."
                )
                await message.answer(
                    "Клиент не был добавлен. Сообщите администратору."
                )
