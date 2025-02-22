from abc import ABC, abstractmethod

from src.schemas.response.client.monthly_full_info_about_client import (
    MonthlyFullInfoAboutClientResponse,
)


class AbstractCollectClientsDataService(ABC):
    @abstractmethod
    async def collect_clients_data(
        self, coach_name: str
    ) -> list[MonthlyFullInfoAboutClientResponse]: ...
