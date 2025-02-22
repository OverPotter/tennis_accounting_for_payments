from src.database.repositories.client_repository import ClientRepository
from src.schemas.response.client.monthly_visits import (
    ClientWithMonthlyVisitsResponse,
)
from src.schemas.response.visit.base import (
    VisitWithCoachNameResponse,
)
from src.services.get_client_visits_in_some_months_service.abc import (
    AbstractGetClientVisitsInSomeMonthsService,
)


class RepositoryGetClientVisitsInSomeMonthsService(
    AbstractGetClientVisitsInSomeMonthsService
):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def get_client_visits_in_3_months(
        self, client_name: str
    ) -> ClientWithMonthlyVisitsResponse:
        client_visits = (
            await self._client_repository.get_client_visits_in_3_months(
                client_name=client_name
            )
        )

        return ClientWithMonthlyVisitsResponse(
            id=client_visits[0][0].id,
            name=client_name,
            visits=[
                VisitWithCoachNameResponse(
                    coach_name=visit[1].coach.name,
                    visit_datetime=visit[1].visit_datetime,
                    training_type=visit[1].training_type.value,
                )
                for visit in client_visits
            ],
        )
