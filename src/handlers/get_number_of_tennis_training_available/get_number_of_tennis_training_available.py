from aiogram import types

from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.handlers.base import BaseCommandHandler
from src.services.get_number_of_tennis_training_available_service.abc import (
    AbstractGetNumberOfTennisTrainingAvailableService,
)
from src.utils.validators.validate_client_name import (
    validate_and_extract_client_name,
)


class GetNumberOfTennisTrainingAvailableCommandHandler(BaseCommandHandler):
    def __init__(
        self,
        get_number_of_tennis_training_available_service: AbstractGetNumberOfTennisTrainingAvailableService,
    ):
        super().__init__()
        self._get_number_of_tennis_training_available_service = (
            get_number_of_tennis_training_available_service
        )

    async def handle(self, message: types.Message) -> None:
        try:
            client_name_parts = message.text.split(" ", 1)

            client_name = validate_and_extract_client_name(
                parts=client_name_parts
            )

            if client_name:
                number_of_trainings = await self._get_number_of_tennis_training_available_service.get_client_number_of_tennis_training_available(
                    client_name=client_name
                )

                if number_of_trainings is not None:
                    self._logger.info(
                        f"Client {client_name} has {number_of_trainings} trainings left."
                    )
                    await message.answer(
                        f"Осталось {number_of_trainings} тренировок."
                    )
                else:
                    self._logger.debug("No remaining trainings found.")
                    await message.answer(
                        "Тренировки не найдены. Сообщите администратору."
                    )

        except ValueError as e:
            self._logger.error(f"Validation failed: {str(e)}")
            await message.answer(f"Данные не валидны: {e}")
        except EntityDoesntExistException as e:
            self._logger.error(f"Client not found: {e.details}")
            await message.answer("Такой клиент не найден.")
