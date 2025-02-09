from abc import ABC, abstractmethod

from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.client.monthly_full_info_about_client import (
    MonthlyFullInfoAboutClientResponse,
)


class AbstractCollectClientsDataService(ABC):
    @abstractmethod
    def collect_clients_data(
        self, clients: list[ClientBaseResponse]
    ) -> MonthlyFullInfoAboutClientResponse: ...
