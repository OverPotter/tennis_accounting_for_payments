from aiogram import types

from src.decorators.error_handler import error_handler
from src.events.visits.create import visit_creation_subject_context
from src.exceptions.validation_exceptions import InvalidVisitDataException
from src.handlers.base import BaseCommandHandler
from src.schemas.payload.visit.base import VisitBasePayloadWithNames
from src.services.create_visit_service.abc import AbstractCreateVisitsService
from src.utils.validators.validate_name import validate_full_name
from src.utils.validators.validate_training_type import validate_training_type
from src.utils.validators.validate_visit_datetime import validate_visit_datetime


class AddVisitsCommandHandler(BaseCommandHandler):
    def __init__(self, create_visits_service: AbstractCreateVisitsService):
        super().__init__()
        self._create_visits_service = create_visits_service

    @error_handler
    async def handle(self, message: types.Message):
        visits = message.text.split("\n")
        for visit in visits:
            visit_payload = self._parse_visits_data(visit)

            async with visit_creation_subject_context() as visit_creation_subject:

                visit_created = await self._create_visits_service.create_visit(
                    payload=visit_payload, subject=visit_creation_subject
                )

                if visit_created:
                    self._logger.info(
                        f"{visit_payload.coach_name}: Visit created for Client='{visit_payload.client_name}', Datetime='{visit_payload.visit_datetime}'."
                    )
                    await message.answer(
                        f"{visit_payload.coach_name}: Визит для клиента {visit_payload.client_name} успешно добавлен."
                    )
                else:
                    self._logger.warning(
                        f"{visit_payload.coach_name}: Failed to create visit for Client='{visit_payload.client_name}', Datetime='{visit_payload.visit_datetime}'."
                    )
                    await message.answer(
                        f"{visit_payload.coach_name}: Ошибка при добавлении визита для клиента {visit_payload.client_name}. Сообщите администратору."
                    )

    @staticmethod
    def _parse_visits_data(
        visits: str,
    ) -> VisitBasePayloadWithNames:
        visits_data_parts = visits.split(" ", 6)

        if len(visits_data_parts) < 7:
            raise InvalidVisitDataException(visits)

        client_name = " ".join(visits_data_parts[:2])
        visit_datetime = " ".join(visits_data_parts[2:4])
        coach_name = " ".join(visits_data_parts[4:6])
        training_type = visits_data_parts[6]

        client_name = validate_full_name(full_name=client_name)
        visit_datetime = validate_visit_datetime(date_and_time=visit_datetime)
        coach_name = validate_full_name(full_name=coach_name)
        training_type = validate_training_type(training_type=training_type)

        return VisitBasePayloadWithNames(
            client_name=client_name,
            coach_name=coach_name,
            visit_datetime=visit_datetime,
            training_type=training_type,
        )
