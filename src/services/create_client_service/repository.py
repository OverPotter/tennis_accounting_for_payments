from pydantic import TypeAdapter

from src.database.repositories.client_repository import ClientRepository
from src.exceptions.entity_exceptions import EntityAlreadyExistException
from src.schemas.response.client.base import ClientBaseResponse
from src.services.create_client_service.abc import AbstractCreateClientService


class RepositoryCreateClientService(AbstractCreateClientService):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def create_client(self, client_name: str) -> ClientBaseResponse:
        is_user_exist = await self._client_repository.get(name=client_name)
        if is_user_exist:
            raise EntityAlreadyExistException(
                key="Name",
                value=client_name,
                entity_name="Client",
            )

        client = await self._client_repository.create(name=client_name)

        return TypeAdapter(ClientBaseResponse).validate_python(client)  # type: ignore
