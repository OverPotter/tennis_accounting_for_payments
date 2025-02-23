from abc import ABC, abstractmethod

from src.schemas.response.client.monthly_income_and_clients_data import (
    MonthlyIncomeAndClientsDataResponse,
)


class AbstractFillInXlsxService(ABC):
    @abstractmethod
    def fill_in_xlsx(
        self,
        total_income_and_clients_data: MonthlyIncomeAndClientsDataResponse,
        filename: str,
    ) -> None: ...
