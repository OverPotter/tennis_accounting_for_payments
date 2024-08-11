from src.database.repositories.payment_repository import PaymentRepository
from src.database.repositories.user_repository import ClientRepository
from src.exceptions.user_exception import UserDoesntExist
from src.services.create_payment_service.abc import AbstractCreatePaymentService


class RepositoryPaymentService(AbstractCreatePaymentService):
    def __init__(
        self,
        client_repository: ClientRepository,
        payment_repository: PaymentRepository,
    ):
        self._client_repository = client_repository
        self._payment_repository = payment_repository

    async def create_payment(
        self, client_name: str, amount: float, payment_date: str
    ) -> bool:
        client = await self._client_repository.get(name=client_name)
        if not client:
            raise UserDoesntExist(details=client_name)

        payment = await self._payment_repository.create(
            client_id=client.id, amount=amount, payment_date=payment_date
        )
        return bool(payment)
