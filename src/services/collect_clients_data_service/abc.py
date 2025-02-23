from abc import ABC, abstractmethod

from src.schemas.response.client.monthly_income_and_clients_data import (
    MonthlyIncomeAndClientsDataResponse,
)


class AbstractCollectClientsDataService(ABC):
    @abstractmethod
    async def collect_clients_data(
        self, coach_name: str, filter_empty: bool = False
    ) -> MonthlyIncomeAndClientsDataResponse: ...
