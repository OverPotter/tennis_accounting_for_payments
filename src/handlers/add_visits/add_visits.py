from aiogram import types
from sqlalchemy.exc import OperationalError

from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.schemas.enums.training_types import TrainingTypesEnum
from src.services.create_visits_service.abc import AbstractCreateVisitsService
from src.services.logging_service.logging_service import Logger
from src.utils.validators.validate_client_name import (
    validate_and_extract_client_name,
)
from src.utils.validators.validate_training_type import (
    validate_and_extract_training_type,
)
from src.utils.validators.validate_visit_datetime import (
    validate_and_extract_visit_datetime,
)


class AddVisitsCommandHandler:
    def __init__(
        self,
        create_visits_service: AbstractCreateVisitsService,
        logger: Logger,
    ):
        self._create_visits_service = create_visits_service
        self._logger = logger

    async def handle(self, message: types.Message):
        visits = message.text.split("\n")
        for visit in visits:
            try:
                client_name, visit_datetime, training_type = (
                    self._parse_visits_data(visit)
                )

                if await self._create_visits_service.create_visits(
                    client_name,
                    visit_datetime,
                    training_type,
                ):
                    self._logger.info(
                        f"Визит для клиента '{client_name}' успешно добавлен."
                    )
                    await message.answer(
                        f"Визит для клиента '{client_name}' успешно добавлен."
                    )
                else:
                    await message.answer(
                        f"Ошибка при добавлении визита для клиента '{client_name}'. Сообщите администратору."
                    )
            except EntityDoesntExistException as e:
                self._logger.error(
                    f"Error: The user named {e.value} was not found."
                )
                await message.answer(
                    f"Ошибка: Пользователь с именем '{e.value}' не найден."
                )
            except OperationalError as e:
                self._logger.error(f"Ошибка при добавлении визита: {e}")
                await message.answer(
                    "Проблемы с добавлением визита. Сообщите администратору."
                )

    @staticmethod
    def _parse_visits_data(visits: str) -> tuple[str, str, TrainingTypesEnum]:
        visits_data_parts = visits.split(" ", 4)
        if len(visits_data_parts) < 3:
            raise ValueError(f"Invalid number of payment data: {visits}")

        client_name = validate_and_extract_client_name(parts=visits_data_parts)
        visit_datetime = validate_and_extract_visit_datetime(
            parts=visits_data_parts
        )
        training_type = validate_and_extract_training_type(
            parts=visits_data_parts
        )

        return client_name, visit_datetime, training_type
