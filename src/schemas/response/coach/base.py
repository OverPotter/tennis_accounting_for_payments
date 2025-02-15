from src.schemas.enums.specializations import SpecializationEnum
from src.schemas.response.base import BaseResponse


class CoachBaseResponse(BaseResponse):
    id: int
    name: str
    specialization: SpecializationEnum
