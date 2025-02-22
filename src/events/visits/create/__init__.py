from contextlib import asynccontextmanager
from typing import AsyncGenerator

from src.database.repositories.manager import (
    OrmRepositoryManager,
    orm_repository_manager_factory,
)
from src.database.repositories.number_of_tennis_training_available_repository import (
    NumberOfTennisTrainingAvailableRepository,
)
from src.events.abc import AbstractSubject
from src.events.base import BaseSubject
from src.events.utils import observer
from src.schemas.payload.number_of_tennis_training.base import (
    NumberOfTennisTrainingBasePayload,
)
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.create_number_of_tennis_training_available_service.abc import (
    AbstractCreateNumberOfTennisTrainingAvailableService,
)
from src.services.create_number_of_tennis_training_available_service.repository import (
    RepositoryCreateNumberOfTennisTrainingAvailableService,
)
from src.services.logging_service.logging_service import Logger, logger_factory


@asynccontextmanager
async def visit_creation_subject_context() -> (
    AsyncGenerator[AbstractSubject[VisitBaseResponse], None]
):
    visit_creation_subject: AbstractSubject[VisitBaseResponse] = BaseSubject()
    logger: Logger = logger_factory()
    repository_manager: OrmRepositoryManager = orm_repository_manager_factory()

    @observer(visit_creation_subject)
    async def _(subject: AbstractSubject[VisitBaseResponse]):
        if subject.state is not None:
            new_visit = subject.state

            async with repository_manager:
                repository: NumberOfTennisTrainingAvailableRepository = (
                    repository_manager.get_number_of_tennis_training_available_repository()
                )

                result = await repository.get_number_by_constraint_pk(
                    client_id=new_visit.client_id,
                    coach_id=new_visit.coach_id,
                    training_type=new_visit.training_type,
                )

                if result:
                    number_of_training = result.number_of_training - 1

                    updated_rowcount = await repository.update(
                        client_id=new_visit.client_id,
                        coach_id=new_visit.coach_id,
                        training_type=new_visit.training_type,
                        number_of_training=number_of_training,
                    )
                    logger.info(
                        f"[Visit Observer] Update {new_visit.training_type.value} training for user with id={new_visit.client_id}."
                    )

                    if updated_rowcount == 0:
                        logger.warning(
                            f"[Visit Observer] Error with save {new_visit}."
                        )
                else:
                    service: (
                        AbstractCreateNumberOfTennisTrainingAvailableService
                    ) = RepositoryCreateNumberOfTennisTrainingAvailableService(
                        number_of_tennis_training_available_repository=repository
                    )
                    number_of_training_for_new_client = -1

                    number_of_tennis_training_payload = NumberOfTennisTrainingBasePayload(
                        client_id=new_visit.client_id,
                        coach_id=new_visit.coach_id,
                        number_of_training=number_of_training_for_new_client,
                        training_type=new_visit.training_type,
                    )

                    created_entity = await service.create_number_of_tennis_training_available(
                        payload=number_of_tennis_training_payload
                    )
                    logger.info(
                        f"[Visit Observer] Coach={new_visit.coach_id}: "
                        f"Create new training for user with id={new_visit.client_id}."
                    )
                    if not created_entity:
                        logger.warning(
                            f"[Visit Observer] Error with save {new_visit}."
                        )

    yield visit_creation_subject
    await visit_creation_subject.notify()
