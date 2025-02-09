from datetime import datetime

from aiogram import types
from sqlalchemy.exc import OperationalError

from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.handlers.base import BaseCommandHandler
from src.schemas.enums.training_types import TrainingTypesEnum
from src.services.create_visit_service.abc import AbstractCreateVisitsService
from src.utils.validators.validate_client_name import (
    validate_and_extract_client_name,
)
from src.utils.validators.validate_training_type import (
    validate_and_extract_training_type,
)
from src.utils.validators.validate_visit_datetime import (
    validate_and_extract_visit_datetime,
)


class AddVisitsCommandHandler(BaseCommandHandler):
    def __init__(self, create_visits_service: AbstractCreateVisitsService):
        super().__init__()
        self._create_visits_service = create_visits_service

    async def handle(self, message: types.Message):
        visits = message.text.split("\n")
        for visit in visits:
            try:
                client_name, visit_datetime, training_type = (
                    self._parse_visits_data(visit)
                )

                if await self._create_visits_service.create_visit(
                    client_name,
                    visit_datetime,
                    training_type,
                ):
                    self._logger.info(
                        f"Visit for client {client_name} has been successfully created."
                    )
                    await message.answer(
                        f"Визит для клиента {client_name} успешно добавлен."
                    )
                else:
                    await message.answer(
                        f"Ошибка при добавлении визита для клиента {client_name}. Сообщите администратору."
                    )
            except EntityDoesntExistException as e:
                self._logger.error(
                    f"Error: The user named {e.value} was not found."
                )
                await message.answer(
                    f"Ошибка: Пользователь с именем {e.value} не найден."
                )
            except ValueError as e:
                self._logger.error(f"Invalid visits data: {e}")
                await message.answer(f"Данные не валидны: {e}")

            except OperationalError as e:
                self._logger.error(f"Problems with database operations: {e}")
                await message.answer(
                    "Проблемы с работой базы данных. Сообщите администратору."
                )

    @staticmethod
    def _parse_visits_data(
        visits: str,
    ) -> tuple[str, datetime, TrainingTypesEnum]:
        visits_data_parts = visits.split(" ", 4)
        if len(visits_data_parts) < 5:
            raise ValueError(f"Invalid number of visit data: {visits}")

        client_name = validate_and_extract_client_name(parts=visits_data_parts)
        visit_datetime = validate_and_extract_visit_datetime(
            parts=visits_data_parts
        )
        training_type = validate_and_extract_training_type(
            parts=visits_data_parts
        )

        return client_name, visit_datetime, training_type
