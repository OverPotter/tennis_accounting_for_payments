from abc import ABC, abstractmethod

from src.schemas.response.client.base import ClientBaseResponse


class AbstractCreateClientService(ABC):
    @abstractmethod
    async def create_client(self, client_name: str) -> ClientBaseResponse: ...
