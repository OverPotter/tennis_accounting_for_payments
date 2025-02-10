from pydantic import TypeAdapter

from src.database.repositories.client_repository import ClientRepository
from src.schemas.response.client.base import ClientBaseResponse
from src.services.get_all_clients_service.abc import (
    AbstractGetAllClientsService,
)


class RepositoryGetAllClientsService(AbstractGetAllClientsService):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def get_all_clients(self) -> list[ClientBaseResponse]:
        clients = await self._client_repository.get_all()

        return [TypeAdapter(ClientBaseResponse).validate_python(client) for client in clients]  # type: ignore
