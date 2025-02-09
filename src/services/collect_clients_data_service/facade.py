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
from src.services.get_client_visits_service.abc import (
    AbstractGetClientVisitsService,
)
from src.services.get_paid_client_training_service.abc import (
    AbstractGetPaidClientTrainingService,
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

    def collect_clients_data(
        self, clients: list[ClientBaseResponse]
    ) -> MonthlyFullInfoAboutClientResponse: ...
