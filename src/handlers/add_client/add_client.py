from aiogram import types

from src.services.create_client_service.abc import AbstractCreateClientService


class AddClientCommandHandler:
    def __init__(
        self,
        create_client_service: AbstractCreateClientService,
    ):
        self._create_client_service = create_client_service

    @staticmethod
    async def handle(message: types.Message):
        await message.answer("Клиент успешно добавлен.")
