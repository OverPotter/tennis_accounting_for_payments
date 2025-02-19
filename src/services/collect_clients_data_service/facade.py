from src.database.repositories.abstract_manager import AbstractRepositoryManager
from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.client.monthly_full_info_about_client import (
    MonthlyFullInfoAboutClientResponse,
)
from src.schemas.response.payment.base import PaymentBaseResponse
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.collect_clients_data_service.abc import (
    AbstractCollectClientsDataService,
)
from src.services.get_all_clients_service.abc import (
    AbstractGetAllClientsService,
)
from src.services.get_all_clients_service.repository import (
    RepositoryGetAllClientsService,
)
from src.services.get_client_visits_service.abc import (
    AbstractGetClientVisitsService,
)
from src.services.get_client_visits_service.repository import (
    RepositoryGetClientVisitsService,
)
from src.services.get_paid_client_training_service.abc import (
    AbstractGetPaidClientTrainingService,
)
from src.services.get_paid_client_training_service.repository import (
    RepositoryGetPaidClientTrainingService,
)
from src.utils.get_training_type_and_number_by_amount import (
    get_training_type_and_number_by_amount,
)


class FacadeCollectClientsDataService(AbstractCollectClientsDataService):
    def __init__(
        self,
        get_all_clients_service: AbstractGetAllClientsService,
        get_client_visits_service: AbstractGetClientVisitsService,
        get_paid_client_training_service: AbstractGetPaidClientTrainingService,
    ):
        self._get_all_clients_service = get_all_clients_service
        self._get_client_visits_service = get_client_visits_service
        self._get_paid_client_training_service = (
            get_paid_client_training_service
        )

    async def collect_clients_data(
        self, coach_name: str
    ) -> list[MonthlyFullInfoAboutClientResponse]:
        clients = await self._get_all_clients_service.get_all_clients()
        result = []

        for client in clients:
            client_paid_training_count_for_all_time = (
                await self._get_client_paid_training_count_for_all_time(
                    client=client, coach_name=coach_name
                )
            )
            client_monthly_payments = await self._get_client_monthly_payments(
                client=client, coach_name=coach_name
            )
            paid_monthly_training = self._calculate_paid_monthly_training(
                client_monthly_payments=client_monthly_payments
            )
            all_client_visits_up_to_current_month = (
                await self._get_client_visits_up_to_current_month(
                    client=client, coach_name=coach_name
                )
            )
            client_visits_info_for_current_month, client_monthly_visits = (
                await self._get_client_visits_info_for_current_month(
                    client=client, coach_name=coach_name
                )
            )

            (
                visits_at_the_beginning_of_the_month,
                visits_at_the_end_of_the_month,
            ) = self._calculate_visits(
                all_client_visits_up_to_current_month,
                client_paid_training_count_for_all_time,
                client_visits_info_for_current_month,
                paid_monthly_training,
            )

            result.append(
                self._create_client_response(
                    client,
                    visits_at_the_beginning_of_the_month,
                    visits_at_the_end_of_the_month,
                    client_monthly_payments,
                    client_monthly_visits,
                )
            )

        return result

    async def _get_client_paid_training_count_for_all_time(
        self, client: ClientBaseResponse, coach_name: str | None = None
    ) -> int:
        return await self._get_paid_client_training_service.get_all_client_paid_training_up_to_current_month(
            client_id=client.id, coach_name=coach_name
        )

    async def _get_client_monthly_payments(
        self, client: ClientBaseResponse, coach_name: str | None = None
    ) -> list[PaymentBaseResponse]:
        return await self._get_paid_client_training_service.get_monthly_paid_client_trainings(
            client_id=client.id, coach_name=coach_name
        )

    @staticmethod
    def _calculate_paid_monthly_training(
        client_monthly_payments: list[PaymentBaseResponse],
    ) -> int:
        return sum(
            count
            for count, _ in (
                get_training_type_and_number_by_amount(payment.amount)
                for payment in client_monthly_payments
            )
            if isinstance(count, int)
        )

    async def _get_client_visits_up_to_current_month(
        self, client: ClientBaseResponse, coach_name: str | None = None
    ) -> int:
        return await self._get_client_visits_service.get_all_client_visits_up_to_current_month(
            client_id=client.id, coach_name=coach_name
        )

    async def _get_client_visits_info_for_current_month(
        self, client: ClientBaseResponse, coach_name: str | None = None
    ) -> tuple[int, list[VisitBaseResponse]]:
        return await self._get_client_visits_service.get_monthly_client_visits(
            client_id=client.id, coach_name=coach_name
        )

    @staticmethod
    def _calculate_visits(
        all_client_visits_up_to_current_month: int,
        client_paid_training_count_for_all_time: int,
        client_visits_info_for_current_month: int,
        paid_monthly_training: int,
    ) -> tuple[int, int]:
        visits_at_the_beginning_of_the_month = (
            client_paid_training_count_for_all_time
            - all_client_visits_up_to_current_month
        )
        visits_at_the_end_of_the_month = (
            visits_at_the_beginning_of_the_month
            - client_visits_info_for_current_month
            + paid_monthly_training
        )
        return (
            visits_at_the_beginning_of_the_month,
            visits_at_the_end_of_the_month,
        )

    @staticmethod
    def _create_client_response(
        client: ClientBaseResponse,
        visits_at_the_beginning_of_the_month: int,
        visits_at_the_end_of_the_month: int,
        client_monthly_payments: list[PaymentBaseResponse],
        client_monthly_visits: list[VisitBaseResponse],
    ) -> MonthlyFullInfoAboutClientResponse:
        return MonthlyFullInfoAboutClientResponse(
            id=client.id,
            name=client.name,
            visits_at_the_beginning_of_the_month=visits_at_the_beginning_of_the_month,
            monthly_payments=client_monthly_payments,
            monthly_visits=client_monthly_visits,
            visits_at_the_end_of_the_month=visits_at_the_end_of_the_month,
        )


def facade_collect_clients_data_factory(
    repository_manager: AbstractRepositoryManager,
) -> FacadeCollectClientsDataService:
    return FacadeCollectClientsDataService(
        get_all_clients_service=RepositoryGetAllClientsService(
            client_repository=repository_manager.get_client_repository()
        ),
        get_client_visits_service=RepositoryGetClientVisitsService(
            visit_repository=repository_manager.get_visits_repository()
        ),
        get_paid_client_training_service=RepositoryGetPaidClientTrainingService(
            payment_repository=repository_manager.get_payment_repository()
        ),
    )
