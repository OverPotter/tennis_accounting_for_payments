from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.payment.base import PaymentBaseResponse
from src.schemas.response.visit.base import VisitBaseResponse


class MonthlyFullInfoAboutClientResponse(ClientBaseResponse):
    visits_at_the_beginning_of_the_month: int
    monthly_payments: list[PaymentBaseResponse]
    monthly_visits: list[VisitBaseResponse]
    visits_at_the_end_of_the_month: int
