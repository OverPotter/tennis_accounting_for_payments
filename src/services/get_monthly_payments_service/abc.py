from abc import ABC, abstractmethod

from src.schemas.response.client.monthly_payments import (
    ClientWithMonthlyPaymentsResponse,
)


class AbstractGetMonthlyPaymentsService(ABC):
    @abstractmethod
    async def get_monthly_payments(
        self, client_name: str
    ) -> ClientWithMonthlyPaymentsResponse: ...
