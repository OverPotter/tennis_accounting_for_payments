import re
from datetime import datetime

from aiogram import types
from sqlalchemy.exc import OperationalError

from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.services.create_payment_service.abc import AbstractCreatePaymentService
from src.services.logging_service.logging_service import Logger


class AddPaymentsCommandHandler:
    def __init__(
        self,
        create_payment_service: AbstractCreatePaymentService,
        logger: Logger,
    ):
        self._create_payment_service = create_payment_service
        self._logger = logger

    async def handle(self, message: types.Message):
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
                        f"Данные для пользователя '{client_name}' сохранены."
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

    def _parse_payment_data(self, payment: str) -> tuple[str, float, str]:
        parts = payment.split(" ", 3)
        if len(parts) < 3:
            raise ValueError(f"Invalid number of payment data: {payment}")

        client_name = self._validate_and_extract_client_name(parts)
        amount = self._validate_and_extract_amount(parts)
        payment_date = self._validate_and_extract_payment_date(parts)

        return client_name, amount, payment_date

    @staticmethod
    def _validate_and_extract_client_name(parts: list[str]) -> str:
        name_parts = parts[:2]
        name_pattern = re.compile(r"^[a-zA-Zа-яА-Я]+$")

        for part in name_parts:
            if not name_pattern.match(part):
                raise ValueError(
                    f"Invalid character(s) in client name part: {part}. Only letters from English or Russian alphabets are allowed."
                )

        return f"{parts[0]} {parts[1]}"

    @staticmethod
    def _validate_and_extract_amount(parts: list[str]) -> float:
        try:
            return float(parts[2])
        except ValueError:
            raise ValueError(
                f"The amount format is incorrect. The amount must be a number: {parts[2]}."
            )

    @staticmethod
    def _validate_and_extract_payment_date(parts: list[str]) -> str:
        if len(parts) == 4 and parts[3].strip():
            payment_date = parts[3].strip()
            try:
                return datetime.strptime(payment_date, "%d.%m.%Y").strftime(
                    "%Y-%m-%d"
                )
            except ValueError:
                raise ValueError(
                    f"The date format is incorrect: {payment_date}. Use the DD.MM.YYYY format."
                )
        else:
            return datetime.now().strftime("%Y-%m-%d")
