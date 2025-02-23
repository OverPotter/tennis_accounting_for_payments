from src.schemas.response.base import BaseResponse
from src.schemas.response.client.monthly_full_info_about_client import (
    MonthlyFullInfoAboutClientResponse,
)


class MonthlyIncomeAndClientsDataResponse(BaseResponse):
    total_income: float
    clients_data: list[MonthlyFullInfoAboutClientResponse]
