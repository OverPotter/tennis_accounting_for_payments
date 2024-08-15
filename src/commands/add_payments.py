from aiogram import Router, types
from aiogram.filters import Command

from src.constants_text import TEXT_OF_MESSAGE_FOR_ADD_PAYMENTS_REQUEST
from src.database.repositories.manager import orm_repository_manager_factory
from src.handlers.add_payments.add_payments import AddPaymentsCommandHandler
from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)
from src.services.logging_service.logging_service import logger_factory

router = Router()


@router.message(Command("add_payments"))
async def add_payment(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_ADD_PAYMENTS_REQUEST,
        reply_markup=types.ForceReply(selective=True),
    )


@router.message()
async def process_payment_data(message: types.Message):
    if (
        message.reply_to_message
        and message.reply_to_message.text
        == TEXT_OF_MESSAGE_FOR_ADD_PAYMENTS_REQUEST
    ):
        repository_manager = orm_repository_manager_factory()
        async with repository_manager:
            handler = AddPaymentsCommandHandler(
                create_payment_service=RepositoryPaymentService(
                    client_repository=repository_manager.get_client_repository(),
                    payment_repository=repository_manager.get_payment_repository(),
                ),
                logger=logger_factory(),
            )
        await handler.handle(message=message)
