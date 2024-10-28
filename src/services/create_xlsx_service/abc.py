from abc import ABC, abstractmethod


class AbstractCreateEmptyTableService(ABC):
    @abstractmethod
    def create_xlsx_table(self) -> None: ...
