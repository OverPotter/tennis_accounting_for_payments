from aiogram import Router, types

from src.constants.messages import (
    TEXT_OF_MESSAGE_FOR_ADD_CLIENT_REQUEST,
    TEXT_OF_MESSAGE_FOR_ADD_COACH_REQUEST,
    TEXT_OF_MESSAGE_FOR_ADD_PAYMENTS_REQUEST,
    TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST,
    TEXT_OF_MESSAGE_FOR_CREATE_REPORT,
    TEXT_OF_MESSAGE_FOR_GET_MONTHLY_PAYMENTS_REQUEST,
    TEXT_OF_MESSAGE_FOR_GET_MONTHLY_VISITS_REQUEST,
    TEXT_OF_MESSAGE_FOR_GET_NUMBER_OF_TENNIS_TRAINING_AVAILABLE_REQUEST,
)
from src.database.repositories.manager import orm_repository_manager_factory
from src.handlers.add_client.add_client import AddClientCommandHandler
from src.handlers.add_coach.add_coach import AddCoachCommandHandler
from src.handlers.add_payments.add_payments import AddPaymentsCommandHandler
from src.handlers.add_visits.add_visits import AddVisitsCommandHandler
from src.handlers.create_report.create_report import CreateReportCommandHandler
from src.handlers.get_client_number_of_tennis_training_available.get_client_number_of_tennis_training_available import (
    GetClientNumberOfTennisTrainingAvailableCommandHandler,
)
from src.handlers.get_client_payments_in_some_months.get_monthly_payments import (
    GetClientPaymentsInSomeMonthsCommandHandler,
)
from src.handlers.get_client_visits_in_some_months_service.get_monthly_visits import (
    GetClientVisitsInSomeMonthsCommandHandler,
)
from src.services.collect_clients_data_service.facade import (
    facade_collect_clients_data_factory,
)
from src.services.create_client_service.repository import (
    RepositoryCreateClientService,
)
from src.services.create_coach_service.repository import (
    RepositoryCreateCoachService,
)
from src.services.create_empty_xlsx_service.create_xlsx import (
    CreateEmptyExcelTableService,
)
from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)
from src.services.create_visit_service.repository import (
    RepositoryCreateVisitsService,
)
from src.services.fill_in_xlsx_service.fill_in_xlsx import FillInXlsxService
from src.services.get_client_payments_in_some_months_service.repository import (
    RepositoryGetClientPaymentsInSomeMonthsService,
)
from src.services.get_client_visits_in_some_months_service.repository import (
    RepositoryGetClientVisitsInSomeMonthsService,
)
from src.services.get_number_of_tennis_training_available_service.repository import (
    RepositoryGetNumberOfTennisTrainingAvailableService,
)
from src.services.send_report_service.telegram import TelegramSendReportService

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
            await handle_client_visits_in_some_months_command(message)
        elif (
            message.reply_to_message.text
            == TEXT_OF_MESSAGE_FOR_GET_NUMBER_OF_TENNIS_TRAINING_AVAILABLE_REQUEST
        ):
            await handle_number_of_tennis_training_available_command(message)
        elif (
            message.reply_to_message.text
            == TEXT_OF_MESSAGE_FOR_GET_MONTHLY_PAYMENTS_REQUEST
        ):
            await handle_client_payments_in_some_months_command(message)
        elif message.reply_to_message.text == TEXT_OF_MESSAGE_FOR_CREATE_REPORT:
            await handle_create_report_command(message)
        elif (
            message.reply_to_message.text
            == TEXT_OF_MESSAGE_FOR_ADD_COACH_REQUEST
        ):
            await handle_coach_command(message)


async def handle_payment_command(message: types.Message):
    async with repository_manager:
        handler = AddPaymentsCommandHandler(
            create_payment_service=RepositoryPaymentService(
                client_repository=repository_manager.get_client_repository(),
                payment_repository=repository_manager.get_payment_repository(),
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


async def handle_coach_command(message: types.Message):
    async with repository_manager:
        handler = AddCoachCommandHandler(
            create_coach_service=RepositoryCreateCoachService(
                coach_repository=repository_manager.get_coach_repository(),
            ),
        )
        await handler.handle(message=message)


async def handle_visits_command(message: types.Message):
    async with repository_manager:
        handler = AddVisitsCommandHandler(
            create_visits_service=RepositoryCreateVisitsService(
                client_repository=repository_manager.get_client_repository(),
                coach_repository=repository_manager.get_coach_repository(),
                visits_repository=repository_manager.get_visits_repository(),
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


async def handle_client_visits_in_some_months_command(
    message: types.Message,
):
    async with repository_manager:
        handler = GetClientVisitsInSomeMonthsCommandHandler(
            get_client_visits_in_some_months_service=RepositoryGetClientVisitsInSomeMonthsService(
                client_repository=repository_manager.get_client_repository(),
            )
        )
        await handler.handle(message=message)


async def handle_client_payments_in_some_months_command(
    message: types.Message,
):
    async with repository_manager:
        handler = GetClientPaymentsInSomeMonthsCommandHandler(
            get_client_payments_in_some_months_service=RepositoryGetClientPaymentsInSomeMonthsService(
                client_repository=repository_manager.get_client_repository(),
            )
        )
        await handler.handle(message=message)


async def handle_create_report_command(
    message: types.Message,
):
    async with repository_manager:
        handler = CreateReportCommandHandler(
            create_empty_xlsx_service=CreateEmptyExcelTableService(),
            collect_clients_data_service=facade_collect_clients_data_factory(
                repository_manager=repository_manager
            ),
            fill_in_xlsx_service=FillInXlsxService(),
            send_report_service=TelegramSendReportService(),
        )
        await handler.handle(message=message)
