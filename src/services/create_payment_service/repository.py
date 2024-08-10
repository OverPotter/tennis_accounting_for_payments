from datetime import datetime

from src.database.repositories.payment_repository import PaymentRepository
from src.database.repositories.user_repository import ClientRepository
from src.services.create_payment_service.abc import AbstractPaymentService


class RepositoryPaymentService(AbstractPaymentService):
    def __init__(
        self,
        client_repository: ClientRepository,
        payment_repository: PaymentRepository,
    ):
        self._client_repository = client_repository
        self._payment_repository = payment_repository

    async def add_payment(
        self, client_name: str, amount: float, payment_date_str: str
    ) -> bool:
        try:
            payment_date = datetime.strptime(
                payment_date_str, "%Y-%m-%d"
            ).date()
        except ValueError:
            return False

        client = await self._client_repository.get(name=client_name)
        if not client:
            return False

        payment = await self._payment_repository.create(
            client_id=client.id, amount=amount, payment_date=payment_date
        )
        return bool(payment)
