from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.visit.base import (
    VisitWithCoachNameResponse,
)


class ClientWithMonthlyVisitsResponse(ClientBaseResponse):
    visits: list[VisitWithCoachNameResponse]
