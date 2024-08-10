from datetime import datetime

from aiogram import Router, types
from aiogram.filters import Command

from src.database.repositories.manager import orm_repository_manager_factory
from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)
from src.services.logging_service.logging_service import logger_factory

router = Router()


@router.message(Command("add_payment"))
async def add_payment(message: types.Message):
    repository_manager = orm_repository_manager_factory()
    async with repository_manager:
        client_repo = repository_manager.get_client_repository()
        payment_repo = repository_manager.get_payment_repository()

        service = RepositoryPaymentService(client_repo, payment_repo)
        logger = logger_factory()

        try:
            command_params = message.text.split()
            client_name = command_params[1]
            amount = float(command_params[2])
            payment_date = datetime.strptime(
                command_params[3], "%Y-%m-%d"
            ).date()

            success = await service.add_payment(
                client_name, amount, payment_date
            )
            if success:
                await message.answer(
                    f"Payment of {amount} added for client {client_name} on {payment_date}."
                )
            else:
                await message.answer(f"Client {client_name} not found.")

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            await message.answer("An error occurred while adding the payment.")
