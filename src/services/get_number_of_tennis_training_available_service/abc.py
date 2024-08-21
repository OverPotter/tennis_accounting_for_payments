from abc import ABC, abstractmethod


class AbstractGetNumberOfTennisTrainingAvailableService(ABC):
    @abstractmethod
    async def get_client_number_of_tennis_training_available(
        self, client_name: str
    ) -> int: ...
