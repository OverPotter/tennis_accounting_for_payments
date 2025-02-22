from src.database.repositories.client_repository import ClientRepository
from src.schemas.response.client.monthly_payments import (
    ClientWithMonthlyPaymentsToCoachesResponse,
)
from src.schemas.response.payment.base import PaymentWithCoachNameResponse
from src.services.get_client_payments_in_some_months_service.abc import (
    AbstractGetClientPaymentsInSomeMonthsService,
)


class RepositoryGetClientPaymentsInSomeMonthsService(
    AbstractGetClientPaymentsInSomeMonthsService
):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def get_client_payments_in_3_months(
        self, client_name: str
    ) -> ClientWithMonthlyPaymentsToCoachesResponse:
        client_payments = (
            await self._client_repository.get_client_payments_in_3_months(
                client_name=client_name
            )
        )

        return ClientWithMonthlyPaymentsToCoachesResponse(
            id=client_payments[0][0].id,
            name=client_name,
            payments=[
                PaymentWithCoachNameResponse(
                    coach_name=payment[1].coach.name,
                    payment_date=payment[1].payment_date,
                    amount=payment[1].amount,
                )
                for payment in client_payments
            ],
        )
