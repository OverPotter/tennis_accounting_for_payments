from abc import ABC, abstractmethod

from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.response.number_of_tennis_training_available.base import (
    NumberOfTennisTrainingAvailableBaseResponse,
)


class AbstractCreateNumberOfTennisTrainingAvailableService(ABC):
    @abstractmethod
    async def create_number_of_tennis_training_available(
        self,
        client_id: int,
        number_of_training: int,
        training_type: TrainingTypesEnum,
    ) -> NumberOfTennisTrainingAvailableBaseResponse: ...
