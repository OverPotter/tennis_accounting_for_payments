from src.database.repositories.remains_repository import RemainsRepository
from src.database.repositories.user_repository import ClientRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.services.get_remains_service.abc import AbstractGetRemainsService


class RepositoryGetClientRemainsService(AbstractGetRemainsService):
    def __init__(
        self,
        client_repository: ClientRepository,
        remains_repository: RemainsRepository,
    ):
        self._client_repository = client_repository
        self._remains_repository = remains_repository

    async def get_client_remains(self, client_name: str) -> int:
        client = await self._client_repository.get_user_with_training_remains(
            client_name=client_name
        )

        if not client:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        total_trainings = sum(
            t.number_of_training for t in client.number_of_trainings_available
        )
        return total_trainings
