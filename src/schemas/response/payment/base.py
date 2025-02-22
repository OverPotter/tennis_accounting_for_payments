from datetime import date

from src.schemas.response.base import BaseResponse


class PaymentBaseResponse(BaseResponse):
    client_id: int
    coach_id: int
    payment_date: date
    amount: float


class PaymentWithCoachNameResponse(BaseResponse):
    coach_name: str
    payment_date: date
    amount: float
