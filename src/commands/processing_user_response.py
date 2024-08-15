from aiogram import Router, types

from src.constants_text import (
    TEXT_OF_MESSAGE_FOR_ADD_CLIENT_REQUEST,
    TEXT_OF_MESSAGE_FOR_ADD_PAYMENTS_REQUEST,
)
from src.database.repositories.manager import orm_repository_manager_factory
from src.handlers.add_client.add_client import AddClientCommandHandler
from src.handlers.add_payments.add_payments import AddPaymentsCommandHandler
from src.services.create_client_service.repository import (
    RepositoryCreateClientService,
)
from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)
from src.services.logging_service.logging_service import logger_factory

router = Router()
logger = logger_factory()
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


async def handle_payment_command(message: types.Message):
    async with repository_manager:
        handler = AddPaymentsCommandHandler(
            create_payment_service=RepositoryPaymentService(
                client_repository=repository_manager.get_client_repository(),
                payment_repository=repository_manager.get_payment_repository(),
            ),
            logger=logger,
        )
        await handler.handle(message=message)


async def handle_client_command(message: types.Message):
    async with repository_manager:
        handler = AddClientCommandHandler(
            create_client_service=RepositoryCreateClientService(
                client_repository=repository_manager.get_client_repository(),
            ),
            logger=logger,
        )
        await handler.handle(message=message)
