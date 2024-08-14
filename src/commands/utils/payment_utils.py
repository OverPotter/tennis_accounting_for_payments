from datetime import datetime as dt

from src.exceptions.user_exception import UserDoesntExist
from src.services.logging_service.logging_service import logger_factory

logger = logger_factory()


def parse_payment_data(payment: str):
    parts = payment.split(" ", 2)
    if len(parts) < 2:
        logger.error(f"Invalid payment data: {payment}")
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
            logger.error(f"Invalid payment date: {payment_date_str}")
            raise ValueError(
                "Неправильный формат даты. Используйте формат dd.mm.yyyy."
            )
    else:
        payment_date = dt.now().strftime("%Y-%m-%d")

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
            logger.error(f"Failed to create payment for client: {client_name}")

    except UserDoesntExist:
        logger.error(f"User {client_name} does not exist.")
        await message.answer(
            f"Ошибка: Пользователь с именем '{client_name}' не найден."
        )
