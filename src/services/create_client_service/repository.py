
from src.database.repositories.client_repository import ClientRepository
from src.schemas.response.client.base import ClientBaseResponse
from src.services.create_client_service.abc import AbstractCreateClientService


class RepositoryCreateClientService(AbstractCreateClientService):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def create_client(self, client_name: str) -> ClientBaseResponse:
        await self._client_repository.check_client_does_not_exist_by_name(
            name=client_name
        )
        client = await self._client_repository.create(name=client_name)

        return ClientBaseResponse.model_validate(client)
