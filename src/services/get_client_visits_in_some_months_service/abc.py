from abc import ABC, abstractmethod

from src.schemas.response.client.monthly_visits import (
    ClientWithMonthlyVisitsResponse,
)


class AbstractGetClientVisitsInSomeMonthsService(ABC):
    @abstractmethod
    async def get_client_visits_in_3_months(
        self, client_name: str
    ) -> ClientWithMonthlyVisitsResponse: ...
