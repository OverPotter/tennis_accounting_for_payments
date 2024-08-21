from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.number_of_tennis_training_available.base import (
    NumberOfTennisTrainingAvailableBaseResponse,
)


class ClientWithTrainingNumberResponse(ClientBaseResponse):
    number_of_trainings_available: list[
        NumberOfTennisTrainingAvailableBaseResponse
    ]
