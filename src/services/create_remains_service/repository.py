from src.database.repositories.remains_repository import RemainsRepository
from src.database.repositories.user_repository import ClientRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.services.create_remains_service.abc import AbstractCreateRemainsService


class RepositoryCreateRemainsService(AbstractCreateRemainsService):
    def __init__(
        self,
        client_repository: ClientRepository,
        remains_repository: RemainsRepository,
    ):
        self._client_repository = client_repository
        self._remains_repository = remains_repository

    async def create_remains(self, client_name: str) -> int:
        client = await self._client_repository.get(name=client_name)
        if not client:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        remains = await self._remains_repository.get(client_id=client.id)

        return remains.number_of_training
