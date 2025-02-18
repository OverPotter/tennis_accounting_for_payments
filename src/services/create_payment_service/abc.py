from abc import ABC, abstractmethod

from src.events.abc import AbstractSubject
from src.schemas.payload.payment.base import PaymentBasePayloadWithName
from src.schemas.response.payment.base import PaymentBaseResponse


class AbstractCreatePaymentService(ABC):
    @abstractmethod
    async def create_payment(
        self,
        payload: PaymentBasePayloadWithName,
        subject: AbstractSubject[PaymentBaseResponse] | None = None,
    ) -> PaymentBaseResponse: ...
