from abc import ABC, abstractmethod


class AbstractCreateClientService(ABC):
    @abstractmethod
    async def create_user(self, tuser_name: str) -> bool: ...
