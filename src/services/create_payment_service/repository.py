from src.database.repositories.client_repository import ClientRepository
from src.database.repositories.coach_repository import CoachRepository
from src.database.repositories.payment_repository import PaymentRepository
from src.events.abc import AbstractSubject
from src.schemas.payload.payment.base import PaymentBasePayloadWithNames
from src.schemas.response.payment.base import PaymentBaseResponse
from src.services.create_payment_service.abc import AbstractCreatePaymentService


class RepositoryPaymentService(AbstractCreatePaymentService):
    def __init__(
        self,
        client_repository: ClientRepository,
        coach_repository: CoachRepository,
        payment_repository: PaymentRepository,
    ):
        self._client_repository = client_repository
        self._coach_repository = coach_repository
        self._payment_repository = payment_repository

    async def create_payment(
        self,
        payload: PaymentBasePayloadWithNames,
        subject: AbstractSubject[PaymentBaseResponse] | None = None,
    ) -> PaymentBaseResponse:

        client = await self._client_repository.get_or_raise_by_name(
            name=payload.client_name
        )

        coach = await self._coach_repository.get_or_raise_by_name(
            name=payload.coach_name
        )

        payment = await self._payment_repository.create(
            client_id=client.id,
            coach_id=coach.id,
            amount=payload.amount,
            payment_date=payload.payment_date,
        )
        created_payment = PaymentBaseResponse.model_validate(payment)

        if subject is not None:
            await subject.update(created_payment)

        return created_payment
