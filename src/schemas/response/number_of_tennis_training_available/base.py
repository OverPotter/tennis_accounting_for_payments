from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.response.base import BaseResponse


class NumberOfTennisTrainingAvailableBaseResponse(BaseResponse):
    client_id: int
    coach_id: int
    number_of_training: int
    training_type: TrainingTypesEnum


class NumberOfTennisTrainingWithCoachNameResponse(BaseResponse):
    coach_name: str
    number_of_training: int
    training_type: TrainingTypesEnum
