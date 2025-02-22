from src.database.repositories.payment_repository import PaymentRepository
from src.schemas.response.payment.base import PaymentBaseResponse
from src.services.get_paid_client_training_service.abc import (
    AbstractGetPaidClientTrainingService,
)
from src.utils.get_first_day_of_current_month import (
    get_first_day_of_current_month,
)
from src.utils.get_last_day_of_current_month import (
    get_last_day_of_current_month,
)
from src.utils.get_training_type_and_number_by_amount import (
    get_training_type_and_number_by_amount,
)


class RepositoryGetPaidClientTrainingService(
    AbstractGetPaidClientTrainingService
):

    def __init__(
        self,
        payment_repository: PaymentRepository,
    ):
        self._payment_repository = payment_repository

    async def get_all_client_paid_training_up_to_current_month(
        self, client_id: int, coach_name: str | None = None
    ) -> int:
        until_what_month = get_first_day_of_current_month()
        client_paid_info = await self._payment_repository.get_all_paid_client_training_up_to_current_month(
            client_id=client_id,
            until_what_month=until_what_month,
            coach_name=coach_name,
        )

        paid_training_count = 0
        for paid_info in client_paid_info:
            paid_training_count += get_training_type_and_number_by_amount(
                paid_info.amount
            )[0]

        return paid_training_count

    async def get_monthly_paid_client_trainings(
        self, client_id: int, coach_name: str | None = None
    ) -> list[PaymentBaseResponse]:
        first_day_of_current_month = get_first_day_of_current_month()
        last_day_of_current_month = get_last_day_of_current_month(
            first_day=first_day_of_current_month
        )
        paid_client_trainings_info_for_current_month = await self._payment_repository.get_monthly_client_paid_training_visits(
            client_id=client_id,
            first_day_of_current_month=first_day_of_current_month,
            last_day_of_current_month=last_day_of_current_month,
            coach_name=coach_name,
        )

        return [
            PaymentBaseResponse.model_validate(paid_info)
            for paid_info in paid_client_trainings_info_for_current_month
        ]
