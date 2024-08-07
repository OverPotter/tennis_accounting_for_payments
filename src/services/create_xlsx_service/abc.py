from abc import ABC, abstractmethod


class AbstractCreateTableService(ABC):
    @staticmethod
    @abstractmethod
    async def create_xlsx_table() -> None: ...
