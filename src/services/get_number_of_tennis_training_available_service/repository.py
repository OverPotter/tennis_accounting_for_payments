from src.database.repositories.number_of_tennis_training_available_repository import (
    NumberOfTennisTrainingAvailableRepository,
)
from src.database.repositories.user_repository import ClientRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.services.get_number_of_tennis_training_available_service.abc import (
    AbstractGetNumberOfTennisTrainingAvailableService,
)


class RepositoryGetNumberOfTennisTrainingAvailableService(
    AbstractGetNumberOfTennisTrainingAvailableService
):
    def __init__(
        self,
        client_repository: ClientRepository,
        number_of_tennis_training_available_repository: NumberOfTennisTrainingAvailableRepository,
    ):
        self._client_repository = client_repository
        self._number_of_tennis_training_available_repository = (
            number_of_tennis_training_available_repository
        )

    async def get_client_number_of_tennis_training_available(
        self, client_name: str
    ) -> int:
        client = await self._client_repository.get_user_with_number_of_tennis_training_available(
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
