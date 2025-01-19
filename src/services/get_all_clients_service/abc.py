from abc import ABC, abstractmethod

from src.schemas.response.client.base import ClientBaseResponse


class AbstractGetAllClientsService(ABC):
    @abstractmethod
    async def get_all_clients(self) -> list[ClientBaseResponse]: ...
