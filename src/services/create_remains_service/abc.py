from abc import ABC, abstractmethod


class AbstractCreateRemainsService(ABC):
    @abstractmethod
    async def create_remains(self, client_name: str) -> int: ...
