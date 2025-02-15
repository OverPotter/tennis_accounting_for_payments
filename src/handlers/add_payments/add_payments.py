from aiogram import types

from src.decorators.error_handler import error_handler
from src.exceptions.validation_exceptions import InvalidPaymentDataException
from src.handlers.base import BaseCommandHandler
from src.schemas.payload.payment.base import PaymentBasePayloadWithName
from src.services.create_payment_service.abc import AbstractCreatePaymentService
from src.utils.validators.validate_amount import validate_amount
from src.utils.validators.validate_name import validate_full_name
from src.utils.validators.validate_payment_date import validate_payment_date


class AddPaymentsCommandHandler(BaseCommandHandler):
    def __init__(
        self,
        create_payment_service: AbstractCreatePaymentService,
    ):
        super().__init__()
        self._create_payment_service = create_payment_service

    @error_handler
    async def handle(self, message: types.Message) -> None:
        payments = message.text.split("\n")

        for payment in payments:
            payment_payload = self._parse_payment_data(payment)

            if await self._create_payment_service.create_payment(
                payload=payment_payload
            ):
                self._logger.info(
                    f"The payment for {payment_payload.client_name} has been successfully created."
                )
                await message.answer(
                    f"Платежные данные для клиента {payment_payload.client_name} сохранены."
                )
            else:
                self._logger.warning(
                    f"Payment for client {payment_payload.client_name} has not been created."
                )
                await message.answer(
                    f"Ошибка при создании платежа для {payment_payload.client_name}. Сообщите администратору."
                )

    @staticmethod
    def _parse_payment_data(payment: str) -> PaymentBasePayloadWithName:
        payment_data_parts = payment.split(" ", 3)

        if len(payment_data_parts) < 3:
            raise InvalidPaymentDataException(payment)

        client_name = " ".join(payment_data_parts[:2])
        amount = payment_data_parts[2]
        payment_date = payment_data_parts[3]

        client_name = validate_full_name(full_name=client_name)
        amount = validate_amount(amount=amount)
        payment_date = validate_payment_date(payment_date=payment_date)

        return PaymentBasePayloadWithName(
            client_name=client_name, payment_date=payment_date, amount=amount
        )
