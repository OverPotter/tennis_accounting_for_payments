from src.commands.utils.payment_utils import (
    handle_payment_creation,
    parse_payment_data,
)
from src.database.repositories.manager import orm_repository_manager_factory
from src.services.create_payment_service.repository import (
    RepositoryPaymentService,
)
from src.services.logging_service.logging_service import Logger


class AddPaymentsCommandFacade:
    def __init__(
        self, logger: Logger, repository_manager: orm_repository_manager_factory
    ):

        self._repository_manager = repository_manager
        self._logger = logger

    async def process_payments(self, payments, message):
        async with self._repository_manager:
            client_repo = self._repository_manager.get_client_repository()
            payment_repo = self._repository_manager.get_payment_repository()
            payment_service = RepositoryPaymentService(
                client_repo, payment_repo
            )

            for payment in payments:
                try:
                    client_name, amount, payment_date = parse_payment_data(
                        payment
                    )
                except ValueError as e:
                    self._logger.error(f"Invalid payment data: {payment}")
                    await message.answer(
                        f"Ошибка: {e} Пожалуйста, введите данные в формате 'Имя Сумма Дата'."
                    )
                    continue

                await handle_payment_creation(
                    payment_service,
                    self._repository_manager,
                    client_name,
                    amount,
                    payment_date,
                    message,
                )
