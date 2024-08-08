from abc import ABC, abstractmethod


class AbstractCreateClientService(ABC):
    @abstractmethod
    async def create_client(self, client_name: str) -> bool: ...
