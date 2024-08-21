from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.response.base import BaseResponse


class NumberOfTennisTrainingAvailableBaseResponse(BaseResponse):
    client_id: int
    number_of_training: int
    training_type: TrainingTypesEnum
