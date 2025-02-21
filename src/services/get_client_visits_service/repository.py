from src.database.repositories.visits_repository import VisitsRepository
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.get_client_visits_service.abc import (
    AbstractGetClientVisitsService,
)
from src.utils.get_first_day_of_current_month import (
    get_first_day_of_current_month,
)
from src.utils.get_last_day_of_current_month import (
    get_last_day_of_current_month,
)


class RepositoryGetClientVisitsService(AbstractGetClientVisitsService):
    def __init__(
        self,
        visit_repository: VisitsRepository,
    ):
        self._visit_repository = visit_repository

    async def get_all_client_visits_up_to_current_month(
        self, client_id: int, coach_name: str | None = None
    ) -> int:
        until_what_month = get_first_day_of_current_month()
        client_visits_info = await self._visit_repository.get_all_client_visits_up_to_current_month(
            client_id=client_id,
            until_what_month=until_what_month,
            coach_name=coach_name,
        )

        return len(client_visits_info)

    async def get_monthly_client_visits(
        self, client_id: int, coach_name: str | None = None
    ) -> tuple[int, list[VisitBaseResponse]]:
        first_day_of_current_month = get_first_day_of_current_month()
        last_day_of_current_month = get_last_day_of_current_month(
            first_day=first_day_of_current_month
        )
        client_visits_info_for_current_month = (
            await self._visit_repository.get_monthly_client_visits(
                client_id=client_id,
                first_day_of_current_month=first_day_of_current_month,
                last_day_of_current_month=last_day_of_current_month,
                coach_name=coach_name,
            )
        )

        return (
            len(client_visits_info_for_current_month),
            [
                VisitBaseResponse.model_validate(visit_info)
                for visit_info in client_visits_info_for_current_month
            ],
        )
