from abc import ABC, abstractmethod


class AbstractGetRemainsService(ABC):
    @abstractmethod
    async def get_client_remains(self, client_name: str) -> int: ...
