from aiogram import Router, types

from src.constants_text import (
    TEXT_OF_MESSAGE_FOR_ADD_CLIENT_REQUEST,
    TEXT_OF_MESSAGE_FOR_ADD_PAYMENTS_REQUEST,
    TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST,
    TEXT_OF_MESSAGE_FOR_GET_MONTHLY_VISITS_REQUEST,
    TEXT_OF_MESSAGE_FOR_GET_NUMBER_OF_TENNIS_TRAINING_AVAILABLE_REQUEST,
)
from src.database.repositories.manager import orm_repository_manager_factory
from src.events.payments.create import payment_creation_subject_context
from src.events.visits.create import visit_creation_subject_context
from src.handlers.add_client.add_client import AddClientCommandHandler
from src.handlers.add_payments.add_payments import AddPaymentsCommandHandler
from src.handlers.add_visits.add_visits import AddVisitsCommandHandler
from src.handlers.get_client_number_of_tennis_training_available.get_client_number_of_tennis_training_available import (
    GetClientNumberOfTennisTrainingAvailableCommandHandler,
)
from src.handlers.get_monthly_visits.get_monthly_visits import (
    GetMonthlyVisitsCommandHandler,
)
from src.services.create_client_service.repository import (
    RepositoryCreateClientService,
)
from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)
from src.services.create_visit_service.repository import (
    RepositoryCreateVisitsService,
)
from src.services.get_monthly_visits.repository import (
    RepositoryGetMonthlyVisitsService,
)
from src.services.get_number_of_tennis_training_available_service.repository import (
    RepositoryGetNumberOfTennisTrainingAvailableService,
)

router = Router()
repository_manager = orm_repository_manager_factory()


@router.message()
async def processing_user_response(message: types.Message):
    if message.reply_to_message:
        if (
            message.reply_to_message.text
            == TEXT_OF_MESSAGE_FOR_ADD_PAYMENTS_REQUEST
        ):
            await handle_payment_command(message)
        elif (
            message.reply_to_message.text
            == TEXT_OF_MESSAGE_FOR_ADD_CLIENT_REQUEST
        ):
            await handle_client_command(message)
        elif (
            message.reply_to_message.text
            == TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST
        ):
            await handle_visits_command(message)
        elif (
            message.reply_to_message.text
            == TEXT_OF_MESSAGE_FOR_GET_MONTHLY_VISITS_REQUEST
        ):
            await handle_monthly_visits_command(message)
        elif (
            message.reply_to_message.text
            == TEXT_OF_MESSAGE_FOR_GET_NUMBER_OF_TENNIS_TRAINING_AVAILABLE_REQUEST
        ):
            await handle_number_of_tennis_training_available_command(message)


async def handle_payment_command(message: types.Message):
    async with payment_creation_subject_context() as payment_creation_subject:
        async with repository_manager:
            handler = AddPaymentsCommandHandler(
                create_payment_service=RepositoryPaymentService(
                    client_repository=repository_manager.get_client_repository(),
                    payment_repository=repository_manager.get_payment_repository(),
                    subject=payment_creation_subject,
                ),
            )
            await handler.handle(message=message)


async def handle_client_command(message: types.Message):
    async with repository_manager:
        handler = AddClientCommandHandler(
            create_client_service=RepositoryCreateClientService(
                client_repository=repository_manager.get_client_repository(),
            ),
        )
        await handler.handle(message=message)


async def handle_visits_command(message: types.Message):
    async with visit_creation_subject_context() as visit_creation_subject:
        async with repository_manager:
            handler = AddVisitsCommandHandler(
                create_visits_service=RepositoryCreateVisitsService(
                    client_repository=repository_manager.get_client_repository(),
                    visits_repository=repository_manager.get_visits_repository(),
                    subject=visit_creation_subject,
                ),
            )
            await handler.handle(message=message)


async def handle_number_of_tennis_training_available_command(
    message: types.Message,
):
    async with repository_manager:
        handler = GetClientNumberOfTennisTrainingAvailableCommandHandler(
            get_number_of_tennis_training_available_service=RepositoryGetNumberOfTennisTrainingAvailableService(
                client_repository=repository_manager.get_client_repository(),
            ),
        )
        await handler.handle(message=message)


async def handle_monthly_visits_command(
    message: types.Message,
):
    async with repository_manager:
        handler = GetMonthlyVisitsCommandHandler(
            get_monthly_visits_service=RepositoryGetMonthlyVisitsService(
                client_repository=repository_manager.get_client_repository(),
            ),
        )
        await handler.handle(message=message)
