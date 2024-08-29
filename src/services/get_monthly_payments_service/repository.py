from src.database.repositories.client_repository import ClientRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.schemas.response.client.monthly_payments import (
    ClientWithMonthlyPaymentsResponse,
)
from src.schemas.response.payment.base import PaymentBaseResponse
from src.services.get_monthly_payments_service.abc import (
    AbstractGetMonthlyPaymentsService,
)


class RepositoryGetMonthlyPaymentsService(AbstractGetMonthlyPaymentsService):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def get_monthly_payments(
        self, client_name: str
    ) -> ClientWithMonthlyPaymentsResponse:
        client = await self._client_repository.get_user_monthly_payments(
            client_name=client_name
        )

        if not client:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        monthly_payments = [
            PaymentBaseResponse(
                client_id=payment.client_id,
                payment_date=payment.payment_date,
                amount=payment.amount,
            )
            for payment in client.payments
        ]

        return ClientWithMonthlyPaymentsResponse(
            name=client.name, payments=monthly_payments
        )
