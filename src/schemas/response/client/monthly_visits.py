from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.visit.base import VisitBaseResponse


class ClientWithMonthlyVisitsResponse(ClientBaseResponse):
    visits: list[VisitBaseResponse]
