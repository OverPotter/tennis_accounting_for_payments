from contextlib import asynccontextmanager
from typing import AsyncGenerator

from src.database.repositories.manager import orm_repository_manager_factory
from src.database.repositories.number_of_tennis_training_available_repository import (
    NumberOfTennisTrainingAvailableRepository,
)
from src.events.abc import AbstractSubject
from src.events.base import BaseSubject
from src.events.utils import observer
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.create_number_of_tennis_training_available_service.abc import (
    AbstractCreateNumberOfTennisTrainingAvailableService,
)
from src.services.create_number_of_tennis_training_available_service.repository import (
    RepositoryCreateNumberOfTennisTrainingAvailableService,
)
from src.services.logging_service.logging_service import logger_factory


@asynccontextmanager
async def visit_creation_subject_context() -> (
    AsyncGenerator[AbstractSubject[VisitBaseResponse], None]
):
    visit_creation_subject: AbstractSubject[VisitBaseResponse] = BaseSubject()
    logger = logger_factory()
    repository_manager = orm_repository_manager_factory()

    @observer(visit_creation_subject)
    async def _(subject: AbstractSubject[VisitBaseResponse]):
        if subject.state is not None:
            new_visit = subject.state

            async with repository_manager:
                repository: NumberOfTennisTrainingAvailableRepository = (
                    repository_manager.get_number_of_tennis_training_available_repository()
                )

                result = (
                    await repository.get_number_by_client_id_and_training_type(
                        client_id=new_visit.client_id,
                        training_type=new_visit.training_type,
                    )
                )

                if result:
                    number_of_training = result.number_of_training - 1

                    updated_rowcount = await repository.update(
                        client_id=new_visit.client_id,
                        training_type=new_visit.training_type,
                        number_of_training=number_of_training,
                    )
                    logger.info(
                        f"[Visit Observer] Update {new_visit.training_type.value} training for user with id={new_visit.client_id}."
                    )

                    if updated_rowcount == 0:
                        logger.error(
                            f"[Visit Observer] Error with save {new_visit}."
                        )
                else:
                    service: (
                        AbstractCreateNumberOfTennisTrainingAvailableService
                    ) = RepositoryCreateNumberOfTennisTrainingAvailableService(
                        number_of_tennis_training_available_repository=repository
                    )
                    number_of_training_for_new_client = -1
                    created_entity = await service.create_number_of_tennis_training_available(
                        client_id=new_visit.client_id,
                        number_of_training=number_of_training_for_new_client,
                        training_type=new_visit.training_type,
                    )
                    logger.info(
                        f"[Visit Observer] Create new training for user with id={new_visit.client_id}."
                    )
                    if not created_entity:
                        logger.error(
                            f"[Visit Observer] Error with save {new_visit}."
                        )

    yield visit_creation_subject
    await visit_creation_subject.notify()
