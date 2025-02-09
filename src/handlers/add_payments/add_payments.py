from datetime import date

from aiogram import types
from sqlalchemy.exc import OperationalError

from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.handlers.base import BaseCommandHandler
from src.services.create_payment_service.abc import AbstractCreatePaymentService
from src.utils.validators.validate_amount import validate_and_extract_amount
from src.utils.validators.validate_client_name import (
    validate_and_extract_client_name,
)
from src.utils.validators.validate_payment_date import (
    validate_and_extract_payment_date,
)


class AddPaymentsCommandHandler(BaseCommandHandler):
    def __init__(
        self,
        create_payment_service: AbstractCreatePaymentService,
    ):
        super().__init__()
        self._create_payment_service = create_payment_service

    async def handle(self, message: types.Message) -> None:
        payments = message.text.split("\n")

        for payment in payments:
            try:
                client_name, amount, payment_date = self._parse_payment_data(
                    payment
                )

                if await self._create_payment_service.create_payment(
                    client_name, amount, payment_date
                ):
                    await message.answer(
                        f"Данные для клиента '{client_name}' сохранены."
                    )
                else:
                    await message.answer(
                        f"Ошибка при создании платежа для '{client_name}'. Сообщите администратору."
                    )
            except EntityDoesntExistException as e:
                self._logger.error(
                    f"Error: The user named {e.value} was not found."
                )
                await message.answer(
                    f"Ошибка: Пользователь с именем '{e.value}' не найден."
                )

            except ValueError as e:
                self._logger.error(f"Invalid payment data: {e}")
                await message.answer(f"Данные не валидны: {e}")

            except OperationalError as e:
                self._logger.error(f"Problems with database operations: {e}")
                await message.answer(
                    "Проблемы с работой базы данных. Сообщите администратору."
                )

    @staticmethod
    def _parse_payment_data(payment: str) -> tuple[str, float, date]:
        payment_data_parts = payment.split(" ", 3)
        if len(payment_data_parts) < 3:
            raise ValueError(f"Invalid number of payment data: {payment}")

        client_name = validate_and_extract_client_name(parts=payment_data_parts)
        amount = validate_and_extract_amount(parts=payment_data_parts)
        payment_date = validate_and_extract_payment_date(
            parts=payment_data_parts
        )

        return client_name, amount, payment_date
