from abc import ABC, abstractmethod


class AbstractCreatePaymentService(ABC):
    @abstractmethod
    async def create_payment(
        self, client_name: str, amount: float, payment_date: str
    ) -> bool: ...
