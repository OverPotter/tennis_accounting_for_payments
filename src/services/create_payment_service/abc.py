from abc import ABC, abstractmethod
from datetime import datetime


class AbstractCreatePaymentService(ABC):
    @abstractmethod
    async def create_payment(
        self, client_name: str, amount: float, payment_date: datetime
    ) -> bool: ...
