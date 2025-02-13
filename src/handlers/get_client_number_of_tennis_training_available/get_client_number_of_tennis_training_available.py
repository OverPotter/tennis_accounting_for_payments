from aiogram import types

from src.decorators.error_handler import error_handler
from src.handlers.base import BaseCommandHandler
from src.services.get_number_of_tennis_training_available_service.abc import (
    AbstractGetNumberOfTennisTrainingAvailableService,
)
from src.utils.create_answer_about_number_training import (
    create_answer_about_number_training,
)
from src.utils.validators.validate_client_name import (
    validate_and_extract_client_name,
)


class GetClientNumberOfTennisTrainingAvailableCommandHandler(
    BaseCommandHandler
):
    def __init__(
        self,
        get_number_of_tennis_training_available_service: AbstractGetNumberOfTennisTrainingAvailableService,
    ):
        super().__init__()
        self._get_number_of_tennis_training_available_service = (
            get_number_of_tennis_training_available_service
        )

    @error_handler
    async def handle(self, message: types.Message) -> None:
        client_name_parts = message.text.split(" ", 1)

        client_name = validate_and_extract_client_name(parts=client_name_parts)

        if client_name:
            client_with_number_of_trainings = await self._get_number_of_tennis_training_available_service.get_client_number_of_tennis_training_available(
                client_name=client_name
            )

            if client_with_number_of_trainings is not None:
                self._logger.info(f"Client {client_name} has trainings.")
                answer_message = create_answer_about_number_training(
                    data=client_with_number_of_trainings
                )
                await message.answer(answer_message)
            else:
                self._logger.warning("No remaining trainings found.")
                await message.answer(
                    "Тренировки не найдены. Сообщите администратору."
                )
