from abc import ABC, abstractmethod

from src.schemas.response.payment.base import PaymentBaseResponse


class AbstractCreatePaymentService(ABC):
    @abstractmethod
    async def create_payment(
        self, client_name: str, amount: float, payment_date: str
    ) -> PaymentBaseResponse: ...
