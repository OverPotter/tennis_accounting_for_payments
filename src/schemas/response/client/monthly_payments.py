from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.payment.base import PaymentBaseResponse


class ClientWithMonthlyPaymentsResponse(ClientBaseResponse):
    payments: list[PaymentBaseResponse]
