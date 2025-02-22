from src.schemas.response.base import BaseResponse


class MonthDetailsBaseResponse(BaseResponse):
    total_days: int
    name: str
    year: int
