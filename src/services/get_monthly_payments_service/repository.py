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

        return ClientWithMonthlyPaymentsResponse(
            id=client_payments[0][0].id,
            name=client_name,
            payments=[
                PaymentBaseResponse(
                    client_id=payment[1].client_id,
                    payment_date=payment[1].payment_date,
                    amount=payment[1].amount,
                )
                for payment in client_payments
            ],
        )
