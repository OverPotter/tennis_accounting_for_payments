from abc import ABC, abstractmethod
from datetime import datetime


class AbstractPaymentService(ABC):
    @abstractmethod
    async def add_payment(
        self, client_name: str, amount: float, payment_date: datetime
    ) -> bool: ...
