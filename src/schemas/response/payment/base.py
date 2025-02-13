from datetime import date

from src.schemas.response.base import BaseResponse


class PaymentBaseResponse(BaseResponse):
    client_id: int
    payment_date: date
    amount: float
