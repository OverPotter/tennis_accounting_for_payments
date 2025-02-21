from src.database.repositories.client_repository import ClientRepository
from src.schemas.response.client.client_with_training_number import (
    ClientWithTrainingNumberResponse,
)
from src.schemas.response.number_of_tennis_training_available.base import (
    NumberOfTennisTrainingAvailableBaseResponse,
)
from src.services.get_number_of_tennis_training_available_service.abc import (
    AbstractGetNumberOfTennisTrainingAvailableService,
)


class RepositoryGetNumberOfTennisTrainingAvailableService(
    AbstractGetNumberOfTennisTrainingAvailableService
):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def get_client_number_of_tennis_training_available(
        self, client_name: str
    ) -> ClientWithTrainingNumberResponse:
        client = await self._client_repository.get_user_with_number_of_tennis_training_available(
            client_name=client_name
        )

        return ClientWithTrainingNumberResponse(
            id=client.id,
            name=client.name,
            number_of_trainings_available=[
                NumberOfTennisTrainingAvailableBaseResponse(
                    client_id=number.client_id,
                    number_of_training=number.number_of_training,
                    training_type=number.training_type,
                )
                for number in client.number_of_trainings_available
            ],
        )
