from aiogram import Router, types
from aiogram.filters import Command

from src.database.repositories.manager import orm_repository_manager_factory
from src.facade.add_payments_facade import AddPaymentsCommandFacade
from src.services.logging_service.logging_service import logger_factory

router = Router()
logger = logger_factory()


repository_manager = orm_repository_manager_factory()

payments_commands = AddPaymentsCommandFacade(logger, repository_manager)


@router.message(Command("add_payments"))
async def add_payment(message: types.Message):
    await message.answer(
        "Введите данные (формат: Имя Сумма Дата, дата в формате dd.mm.yyyy):",
        reply_markup=types.ForceReply(selective=True),
    )


@router.message()
async def process_payment_data(message: types.Message):
    if (
        message.reply_to_message
        and message.reply_to_message.text
        == "Введите данные (формат: Имя Сумма Дата, дата в формате dd.mm.yyyy):"
    ):
        data = message.text
        payments = data.split("\n")

        await payments_commands.process_payments(payments, message)
