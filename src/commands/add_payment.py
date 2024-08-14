from datetime import datetime
from datetime import datetime as dt

from aiogram import Router, types
from aiogram.filters import Command

from src.database.repositories.manager import orm_repository_manager_factory
from src.exceptions.user_exception import UserDoesntExist
from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)

router = Router()


@router.message(Command("create_payments"))
async def create_payment(message: types.Message):
    await message.answer(
        "Введите данные пользователя (формат: Имя Сумма Дата, дата в формате dd.mm.yyyy):",
        reply_markup=types.ForceReply(selective=True),
    )


def parse_payment_data(payment: str):
    parts = payment.split(" ", 2)
    if len(parts) < 2:
        raise ValueError("Неправильный формат данных.")

    client_name = parts[0]
    amount = float(parts[1])

    if len(parts) == 3 and parts[2].strip():
        payment_date_str = parts[2].strip()
        try:
            payment_date = dt.strptime(payment_date_str, "%d.%m.%Y").strftime(
                "%Y-%m-%d"
            )
        except ValueError:
            raise ValueError(
                "Неправильный формат даты. Используйте формат dd.mm.yyyy."
            )
    else:
        payment_date = datetime.now().strftime("%Y-%m-%d")

    return client_name, amount, payment_date


async def handle_payment_creation(
    payment_service,
    repository_manager,
    client_name,
    amount,
    payment_date,
    message,
):
    try:
        payment_created = await payment_service.create_payment(
            client_name, amount, payment_date
        )

        if payment_created:
            await repository_manager.commit()
            await message.answer(
                f"Данные для пользователя '{client_name}' сохранены."
            )
        else:
            await message.answer(
                f"Ошибка при создании платежа для '{client_name}'. Попробуйте снова."
            )
    except UserDoesntExist:
        await message.answer(
            f"Ошибка: Пользователь с именем '{client_name}' не найден."
        )


@router.message()
async def process_payment_data(message: types.Message):
    if (
        message.reply_to_message
        and message.reply_to_message.text
        == "Введите данные пользователя (формат: Имя Сумма Дата, дата в формате dd.mm.yyyy):"
    ):
        data = message.text
        payments = data.split("\n")

        repository_manager = orm_repository_manager_factory()
        async with repository_manager:
            client_repo = repository_manager.get_client_repository()
            payment_repo = repository_manager.get_payment_repository()
            payment_service = RepositoryPaymentService(
                client_repo, payment_repo
            )

            for payment in payments:
                try:
                    client_name, amount, payment_date = parse_payment_data(
                        payment
                    )
                except ValueError as e:
                    await message.answer(
                        f"Ошибка: {e} Пожалуйста, введите данные в формате 'Имя Сумма Дата'."
                    )
                    continue

                await handle_payment_creation(
                    payment_service,
                    repository_manager,
                    client_name,
                    amount,
                    payment_date,
                    message,
                )
