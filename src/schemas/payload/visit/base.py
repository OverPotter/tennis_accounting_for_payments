from datetime import datetime

from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.payload.base import BasePayload


class VisitBasePayloadWithNames(BasePayload):
    client_name: str
    coach_name: str
    visit_datetime: datetime
    training_type: TrainingTypesEnum
