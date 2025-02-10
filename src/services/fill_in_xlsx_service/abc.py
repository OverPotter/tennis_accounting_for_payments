from abc import ABC, abstractmethod

from src.schemas.response.client.monthly_full_info_about_client import (
    MonthlyFullInfoAboutClientResponse,
)


class AbstractFillInXlsxService(ABC):
    @abstractmethod
    def fill_in_xlsx(
        self, clients: list[MonthlyFullInfoAboutClientResponse], filename: str
    ) -> None: ...
