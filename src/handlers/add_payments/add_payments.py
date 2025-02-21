from aiogram import types

from src.decorators.error_handler import error_handler
from src.events.payments.create import payment_creation_subject_context
from src.exceptions.validation_exceptions import InvalidPaymentDataException
from src.handlers.base import BaseCommandHandler
from src.schemas.payload.payment.base import PaymentBasePayloadWithNames
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

            async with payment_creation_subject_context() as payment_creation_subject:
                if await self._create_payment_service.create_payment(
                    payload=payment_payload, subject=payment_creation_subject
                ):
                    self._logger.info(
                        f"Payment for {payment_payload.client_name} was successfully created by the coach {payment_payload.coach_name}."
                    )
                    await message.answer(
                        f"Платежные данные для клиента {payment_payload.client_name} сохранены тренером {payment_payload.coach_name}."
                    )
                else:
                    self._logger.warning(
                        f"Payment for client {payment_payload.client_name} has not been created by the coach {payment_payload.coach_name}."
                    )
                    await message.answer(
                        f"Ошибка при создании платежа для клиента {payment_payload.client_name} тренером {payment_payload.coach_name}. Сообщите администратору."
                    )

    @staticmethod
    def _parse_payment_data(payment: str) -> PaymentBasePayloadWithNames:
        payment_data_parts = payment.split(" ", 5)

        if len(payment_data_parts) < 5:
            raise InvalidPaymentDataException(payment)

        client_name = " ".join(payment_data_parts[:2])
        amount = payment_data_parts[2]
        payment_date = payment_data_parts[3]
        coach_name = " ".join(payment_data_parts[4:])

        client_name = validate_full_name(full_name=client_name)
        amount = validate_amount(amount=amount)
        payment_date = validate_payment_date(payment_date=payment_date)
        coach_name = validate_full_name(full_name=coach_name)

        return PaymentBasePayloadWithNames(
            client_name=client_name,
            coach_name=coach_name,
            payment_date=payment_date,
            amount=amount,
        )
