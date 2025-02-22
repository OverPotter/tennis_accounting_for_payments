from abc import ABC, abstractmethod

from src.schemas.payload.number_of_tennis_training.base import (
    NumberOfTennisTrainingBasePayload,
)
from src.schemas.response.number_of_tennis_training_available.base import (
    NumberOfTennisTrainingAvailableBaseResponse,
)


class AbstractCreateNumberOfTennisTrainingAvailableService(ABC):
    @abstractmethod
    async def create_number_of_tennis_training_available(
        self, payload: NumberOfTennisTrainingBasePayload
    ) -> NumberOfTennisTrainingAvailableBaseResponse: ...
