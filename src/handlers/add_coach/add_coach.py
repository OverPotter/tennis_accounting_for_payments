from aiogram import types

from src.decorators.error_handler import error_handler
from src.handlers.base import BaseCommandHandler
from src.schemas.payload.coach.base import CoachBasePayload
from src.services.create_coach_service.abc import AbstractCreateCoachService
from src.utils.validators.validate_name import validate_and_extract_name
from src.utils.validators.validate_specialization import validate_specialization


class AddCoachCommandHandler(BaseCommandHandler):
    def __init__(self, create_coach_service: AbstractCreateCoachService):
        super().__init__()
        self._create_coach_service = create_coach_service

    @error_handler
    async def handle(self, message: types.Message) -> None:
        coach_data = message.text.split(" ", 2)

        coach_name = validate_and_extract_name(parts=coach_data[:-1])
        specialization = validate_specialization(specialization=coach_data[-1])

        if coach_name:

            if await self._create_coach_service.create_coach(
                payload=CoachBasePayload(
                    name=coach_name, specialization=specialization
                )
            ):
                self._logger.info(
                    f"The coach {coach_name} with specialization {specialization} has been successfully created."
                )
                await message.answer("Тренер успешно добавлен.")

            else:
                self._logger.warning(
                    f"The coach {coach_name} with specialization {specialization} has not been created."
                )
                await message.answer(
                    "Тренер не был добавлен. Сообщите администратору."
                )
