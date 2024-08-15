from datetime import datetime

from src.exceptions.entity_exceptions import (
    EntityDoesntExistException,
    VisitCreationException,
)
from src.schemas.enums.training_types import TrainingTypesEnum
from src.services.create_visits_service.abc import AbstractCreateVisitsService
from src.services.logging_service.logging_service import Logger


class AddVisitsCommandHandler:
    def __init__(
        self,
        create_visits_service: AbstractCreateVisitsService,
        logger: Logger,
    ):
        self._create_visits_service = create_visits_service
        self._logger = logger

    def _parse_training_type(self, training_type: str) -> str:
        meaning = {
            "индив": TrainingTypesEnum.INDIVIDUAL_TRAINING,
            "сплит": TrainingTypesEnum.SPLIT_TRAINING,
            "группа": TrainingTypesEnum.GROUP_TRAINING,
        }
        try:
            return meaning[training_type]
        except KeyError:
            self._logger.error(f"Недопустимый тип тренировки: {training_type}.")
            raise ValueError(
                f"Недопустимый тип тренировки: {training_type}. Доступные значения: 'индив', 'сплит', 'группа'."
            )

    def _validate_visit_datetime(self, visit_datetime: str) -> str:
        try:
            dt = datetime.strptime(visit_datetime, "%d.%m.%Y %H:%M")
            return dt.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            self._logger.error(
                f"Некорректный формат даты и времени: {visit_datetime}."
            )
            raise ValueError(
                "Некорректный формат даты и времени. Используйте формат 'dd.mm.yyyy HH:MM'."
            )

    async def handle_add_visit(
        self, client_name: str, visit_datetime: str, training_type: str
    ) -> bool:

        visit_dt = self._validate_visit_datetime(visit_datetime)
        training_type_enum = self._parse_training_type(training_type)

        try:
            success = await self._create_visits_service.create_visits(
                client_name=client_name,
                visit_datetime=visit_dt,
                training_type=training_type_enum,
            )
            if success:
                self._logger.info(
                    f"Визит для клиента '{client_name}' успешно добавлен."
                )
            return success
        except EntityDoesntExistException as e:
            self._logger.error(f"Клиент '{client_name}' не найден: {e}")
        except VisitCreationException as e:
            self._logger.error(f"Ошибка при добавлении визита: {e}")
