from abc import ABC, abstractmethod

from src.schemas.response.client.monthly_payments import (
    ClientWithMonthlyPaymentsToCoachesResponse,
)


class AbstractGetClientPaymentsInSomeMonthsService(ABC):
    @abstractmethod
    async def get_client_payments_in_3_months(
        self, client_name: str
    ) -> ClientWithMonthlyPaymentsToCoachesResponse: ...
