from abc import ABC, abstractmethod


class AbstractCreateEmptyTableService(ABC):
    @abstractmethod
    async def create_xlsx_table(self) -> str: ...
