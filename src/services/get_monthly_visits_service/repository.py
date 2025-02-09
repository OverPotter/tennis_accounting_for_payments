from src.database.repositories.client_repository import ClientRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.schemas.response.client.monthly_visits import (
    ClientWithMonthlyVisitsResponse,
)
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.get_monthly_visits_service.abc import (
    AbstractGetMonthlyVisitsService,
)


class RepositoryGetMonthlyVisitsService(AbstractGetMonthlyVisitsService):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def get_monthly_visits(
        self, client_name: str
    ) -> ClientWithMonthlyVisitsResponse:
        client_visits = await self._client_repository.get_user_monthly_visits(
            client_name=client_name
        )

        if not client_visits:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        return ClientWithMonthlyVisitsResponse(
            id=client_visits[0][0].id,
            name=client_name,
            visits=[
                VisitBaseResponse(
                    client_id=visit[1].client_id,
                    visit_datetime=visit[1].visit_datetime,
                    training_type=visit[1].training_type.value,
                )
                for visit in client_visits
            ],
        )
