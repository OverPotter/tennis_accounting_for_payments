from src.database.repositories.number_of_tennis_training_available_repository import (
    NumberOfTennisTrainingAvailableRepository,
)
from src.schemas.payload.number_of_tennis_training.base import (
    NumberOfTennisTrainingBasePayload,
)
from src.schemas.response.number_of_tennis_training_available.base import (
    NumberOfTennisTrainingAvailableBaseResponse,
)
from src.services.create_number_of_tennis_training_available_service.abc import (
    AbstractCreateNumberOfTennisTrainingAvailableService,
)


class RepositoryCreateNumberOfTennisTrainingAvailableService(
    AbstractCreateNumberOfTennisTrainingAvailableService
):
    def __init__(
        self,
        number_of_tennis_training_available_repository: NumberOfTennisTrainingAvailableRepository,
    ):
        self._number_of_tennis_training_available_repository = (
            number_of_tennis_training_available_repository
        )

    async def create_number_of_tennis_training_available(
        self, payload: NumberOfTennisTrainingBasePayload
    ) -> NumberOfTennisTrainingAvailableBaseResponse:

        number_of_tennis_training = (
            await self._number_of_tennis_training_available_repository.create(
                **payload.model_dump()
            )
        )
        created_number_of_tennis_training = (
            NumberOfTennisTrainingAvailableBaseResponse.model_validate(
                number_of_tennis_training
            )
        )

        return created_number_of_tennis_training
