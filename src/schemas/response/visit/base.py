from datetime import datetime

from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.response.base import BaseResponse


class VisitBaseResponse(BaseResponse):
    client_id: int
    coach_id: int
    visit_datetime: datetime
    training_type: TrainingTypesEnum


class VisitWithCoachNameResponse(BaseResponse):
    coach_name: str
    visit_datetime: datetime
    training_type: TrainingTypesEnum
