from datetime import date

from src.schemas.payload.base import BasePayload


class PaymentBasePayloadWithNames(BasePayload):
    client_name: str
    coach_name: str
    payment_date: date
    amount: float
