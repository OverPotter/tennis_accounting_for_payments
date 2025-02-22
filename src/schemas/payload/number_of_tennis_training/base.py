from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.payload.base import BasePayload


class NumberOfTennisTrainingBasePayload(BasePayload):
    client_id: int
    coach_id: int
    number_of_training: int
    training_type: TrainingTypesEnum
