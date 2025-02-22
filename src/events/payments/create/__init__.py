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
from src.schemas.response.payment.base import PaymentBaseResponse
from src.services.create_number_of_tennis_training_available_service.abc import (
    AbstractCreateNumberOfTennisTrainingAvailableService,
)
from src.services.create_number_of_tennis_training_available_service.repository import (
    RepositoryCreateNumberOfTennisTrainingAvailableService,
)
from src.services.logging_service.logging_service import Logger, logger_factory
from src.utils.get_training_type_and_number_by_amount import (
    get_training_type_and_number_by_amount,
)


@asynccontextmanager
async def payment_creation_subject_context() -> (
    AsyncGenerator[AbstractSubject[PaymentBaseResponse], None]
):
    payment_creation_subject: AbstractSubject[PaymentBaseResponse] = (
        BaseSubject()
    )
    logger: Logger = logger_factory()
    repository_manager: OrmRepositoryManager = orm_repository_manager_factory()

    @observer(payment_creation_subject)
    async def _(subject: AbstractSubject[PaymentBaseResponse]):
        if subject.state is not None:
            new_payment = subject.state

            number_of_training_for_price, training_type = (
                get_training_type_and_number_by_amount(
                    amount=new_payment.amount
                )
            )

            async with repository_manager:
                repository: NumberOfTennisTrainingAvailableRepository = (
                    repository_manager.get_number_of_tennis_training_available_repository()
                )

                result = await repository.get_number_by_constraint_pk(
                    client_id=new_payment.client_id,
                    coach_id=new_payment.coach_id,
                    training_type=training_type,
                )

                if result:
                    number_of_training = (
                        result.number_of_training + number_of_training_for_price
                    )
                    updated_rowcount = await repository.update(
                        client_id=new_payment.client_id,
                        coach_id=new_payment.coach_id,
                        training_type=training_type,
                        number_of_training=number_of_training,
                    )
                    logger.info(
                        f"[Payment Observer] Coach={new_payment.coach_id}: Update {training_type} training for user with id={new_payment.client_id}."
                    )

                    if updated_rowcount == 0:
                        logger.warning(
                            f"[Payment Observer] Error with save {new_payment}."
                        )
                else:
                    service: (
                        AbstractCreateNumberOfTennisTrainingAvailableService
                    ) = RepositoryCreateNumberOfTennisTrainingAvailableService(
                        number_of_tennis_training_available_repository=repository
                    )

                    number_of_tennis_training_payload = (
                        NumberOfTennisTrainingBasePayload(
                            client_id=new_payment.client_id,
                            coach_id=new_payment.coach_id,
                            number_of_training=number_of_training_for_price,
                            training_type=training_type,
                        )
                    )

                    created_entity = await service.create_number_of_tennis_training_available(
                        payload=number_of_tennis_training_payload
                    )
                    logger.info(
                        f"[Payment Observer] Coach={new_payment.coach_id}: "
                        f"Create new available training for user with id={new_payment.client_id}."
                    )
                    if not created_entity:
                        logger.warning(
                            f"[Payment Observer] Error with save {new_payment}."
                        )

    yield payment_creation_subject
    await payment_creation_subject.notify()
