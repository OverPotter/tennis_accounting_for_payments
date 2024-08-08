from src.database.repositories.user_repository import ClientRepository
from src.services.create_client_service.abc import AbstractCreateClientService


class RepositoryCreateClientService(AbstractCreateClientService):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def create_client(self, client_name: str) -> bool:
        is_create = await self._client_repository.get(name=client_name)
        if is_create:
            return True

        client = await self._client_repository.create(name=client_name)

        return bool(client)
