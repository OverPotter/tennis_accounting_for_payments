from abc import ABC, abstractmethod

from src.schemas.response.client.client_with_training_number import (
    ClientWithTrainingNumberResponse,
)


class AbstractGetNumberOfTennisTrainingAvailableService(ABC):
    @abstractmethod
    async def get_client_number_of_tennis_training_available(
        self, client_name: str
    ) -> ClientWithTrainingNumberResponse: ...
