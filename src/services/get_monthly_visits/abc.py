from abc import ABC, abstractmethod

from src.schemas.response.visit.monthly_visits import (
    ClientWithMonthlyVisitsResponse,
)


class AbstractGetMonthlyVisitsService(ABC):
    @abstractmethod
    async def get_monthly_visits(
        self, client_name: str
    ) -> ClientWithMonthlyVisitsResponse: ...