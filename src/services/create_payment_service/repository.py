from src.database.repositories.client_repository import ClientRepository
from src.database.repositories.payment_repository import PaymentRepository
from src.events.abc import AbstractSubject
from src.schemas.payload.payment.base import PaymentBasePayloadWithName
from src.schemas.response.payment.base import PaymentBaseResponse
from src.services.create_payment_service.abc import AbstractCreatePaymentService
from src.utils.get_entity import get_entity


class RepositoryPaymentService(AbstractCreatePaymentService):
    def __init__(
        self,
        client_repository: ClientRepository,
        payment_repository: PaymentRepository,
    ):
        self._client_repository = client_repository
        self._payment_repository = payment_repository

    async def create_payment(
        self,
        payload: PaymentBasePayloadWithName,
        subject: AbstractSubject[PaymentBaseResponse] | None = None,
    ) -> PaymentBaseResponse:

        client = await get_entity(
            repository=self._client_repository,
            name=payload.client_name,
            entity_name="Client",
        )

        payment = await self._payment_repository.create(
            client_id=client.id,
            amount=payload.amount,
            payment_date=payload.payment_date,
        )
        created_payment = PaymentBaseResponse.model_validate(payment)

        if subject is not None:
            await subject.update(created_payment)

        return created_payment
