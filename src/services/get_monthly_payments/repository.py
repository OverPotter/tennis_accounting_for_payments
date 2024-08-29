from src.database.repositories.client_repository import ClientRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.schemas.response.client.monthly_payments import (
    ClientWithMonthlyPaymentsResponse,
)
from src.schemas.response.payment.base import PaymentBaseResponse
from src.services.get_monthly_payments.abc import (
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
        client_payments = (
            await self._client_repository.get_user_monthly_payments(
                client_name=client_name
            )
        )

        if not client_payments:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        monthly_payments = [
            PaymentBaseResponse(
                client_id=row[0],
                payment_date=row[1],
                amount=row[2],
            )
            for row in client_payments
        ]

        return ClientWithMonthlyPaymentsResponse(
            name=client_name, payments=monthly_payments
        )
