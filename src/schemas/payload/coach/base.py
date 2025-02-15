from src.schemas.enums.specializations import SpecializationEnum
from src.schemas.payload.base import BasePayload


class CoachBasePayload(BasePayload):
    name: str
    specialization: SpecializationEnum
