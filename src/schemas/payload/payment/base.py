from datetime import date

from src.schemas.payload.base import BasePayload


class PaymentBasePayloadWithName(BasePayload):
    client_name: str
    payment_date: date
    amount: float
