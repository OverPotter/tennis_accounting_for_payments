from src.database.repositories.abstract_manager import AbstractRepositoryManager
from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.client.monthly_full_info_about_client import (
    MonthlyFullInfoAboutClientResponse,
)
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
        self, clients: list[ClientBaseResponse]
    ) -> list[MonthlyFullInfoAboutClientResponse]:
        clients = await self._get_all_clients_service.get_all_clients()
        result = []

        # todo: solve issue with N+1
        for client in clients:
            client_paid_training_count_for_all_time = await self._get_paid_client_training_service.get_all_client_paid_training_up_to_current_month(
                client_id=client.id
            )
            client_monthly_payments = await self._get_paid_client_training_service.get_monthly_paid_client_trainings(
                client_id=client.id
            )

            all_client_visits_up_to_current_month = await self._get_client_visits_service.get_all_client_visits_up_to_current_month(
                client_id=client.id
            )
            client_visits_info_for_current_month, client_monthly_visits = (
                await self._get_client_visits_service.get_monthly_client_visits(
                    client_id=client.id
                )
            )

            visits_at_the_beginning_of_the_month = (
                all_client_visits_up_to_current_month
                - client_paid_training_count_for_all_time
            )
            visits_at_the_end_of_the_month = (
                visits_at_the_beginning_of_the_month
                - client_visits_info_for_current_month
            )

            result.append(
                MonthlyFullInfoAboutClientResponse(
                    id=client.id,
                    name=client.name,
                    visits_at_the_beginning_of_the_month=visits_at_the_beginning_of_the_month,
                    monthly_payments=client_monthly_payments,
                    monthly_visits=client_monthly_visits,
                    visits_at_the_end_of_the_month=visits_at_the_end_of_the_month,
                )
            )

        return result


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
