from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.payment.base import (
    PaymentWithCoachNameResponse,
)


class ClientWithMonthlyPaymentsToCoachesResponse(ClientBaseResponse):
    payments: list[PaymentWithCoachNameResponse]
