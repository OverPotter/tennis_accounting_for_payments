from datetime import date

from pydantic import TypeAdapter

from src.database.repositories.client_repository import ClientRepository
from src.database.repositories.payment_repository import PaymentRepository
from src.events.abc import AbstractSubject
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.schemas.response.payment.base import PaymentBaseResponse
from src.services.create_payment_service.abc import AbstractCreatePaymentService


class RepositoryPaymentService(AbstractCreatePaymentService):
    def __init__(
        self,
        client_repository: ClientRepository,
        payment_repository: PaymentRepository,
        subject: AbstractSubject[PaymentBaseResponse] | None = None,
    ):
        self._client_repository = client_repository
        self._payment_repository = payment_repository
        self._subject = subject

    async def create_payment(
        self, client_name: str, amount: float, payment_date: date
    ) -> PaymentBaseResponse:

        client = await self._client_repository.get(name=client_name)
        if not client:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        payment = await self._payment_repository.create(
            client_id=client.id, amount=amount, payment_date=payment_date
        )
        created_payment = TypeAdapter(PaymentBaseResponse).validate_python(payment)  # type: ignore

        if self._subject is not None:
            await self._subject.update(created_payment)

        return created_payment
