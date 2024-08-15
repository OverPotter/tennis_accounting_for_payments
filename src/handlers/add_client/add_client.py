from aiogram import types

from src.exceptions.entity_exceptions import EntityAlreadyExistException
from src.services.create_client_service.abc import AbstractCreateClientService
from src.services.logging_service.logging_service import Logger


class AddClientCommandHandler:
    def __init__(
        self,
        create_client_service: AbstractCreateClientService,
        logger: Logger,
    ):
        self._create_client_service = create_client_service
        self._logger = logger

    async def handle(self, message: types.Message):
        try:
            client_name = await self._validate_client_name(message=message)

            if client_name:

                if await self._create_client_service.create_client(
                    client_name=client_name
                ):
                    self._logger.info(
                        "The client has been successfully created."
                    )
                    await message.answer("Клиент успешно добавлен.")

                else:
                    self._logger.debug("The client has not been created.")

            else:
                self._logger.error("Validation failed: invalid client name.")

        except ValueError as e:
            self._logger.error(f"Validation failed: {str(e)}")
        except EntityAlreadyExistException as e:
            self._logger.error(f"User already exist: {e.details}")
            await message.answer("Такой пользователь уже существует.")

    @staticmethod
    async def _validate_client_name(message: types.Message) -> str:
        client_name = message.text[len("/add_client") :].strip()
        words = client_name.split()

        error_msg = None
        if len(words) != 2:
            error_msg = "Пожалуйста, укажите имя и фамилию в два слова."
        elif not all(word.isalpha() for word in words):
            error_msg = "Имя и фамилия должны содержать только буквы."

        if error_msg:
            await message.answer(error_msg)
            raise ValueError(error_msg)

        return client_name
