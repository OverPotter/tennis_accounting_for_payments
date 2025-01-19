from src.schemas.response.client.base import ClientBaseResponse
from src.schemas.response.client.monthly_full_info_about_client import (
    MonthlyFullInfoAboutClientResponse,
)
from src.services.collect_client_data_service.abc import (
    AbstractCollectClientDataService,
)
from src.services.get_client_visits_service.abc import (
    AbstractGetClientVisitsService,
)
from src.services.get_paid_client_training_service.abc import (
    AbstractGetPaidClientTrainingService,
)


class FacadeCollectClientDataService(AbstractCollectClientDataService):
    def __init__(
        self,
        get_client_visits_service: AbstractGetClientVisitsService,
        get_paid_client_training_service: AbstractGetPaidClientTrainingService,
    ):
        self._get_client_visits_service = get_client_visits_service
        self._get_paid_client_training_service = (
            get_paid_client_training_service
        )

    def collect_client_data(
        self, client: ClientBaseResponse
    ) -> MonthlyFullInfoAboutClientResponse: ...
