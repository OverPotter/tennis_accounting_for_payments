from src.database.repositories.client_repository import ClientRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.schemas.response.client.monthly_visits import (
    ClientWithMonthlyVisitsResponse,
)
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.get_monthly_visits.abc import AbstractGetMonthlyVisitsService


class RepositoryGetMonthlyVisitsService(AbstractGetMonthlyVisitsService):
    def __init__(
        self,
        client_repository: ClientRepository,
    ):
        self._client_repository = client_repository

    async def get_monthly_visits(
        self, client_name: str
    ) -> ClientWithMonthlyVisitsResponse:
        client = await self._client_repository.get_user_monthly_visits(
            client_name=client_name
        )

        if not client:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        monthly_visits = [
            VisitBaseResponse(
                client_id=visit.client_id,
                visit_datetime=visit.visit_datetime,
                training_type=visit.training_type,
            )
            for visit in client.visits
        ]

        return ClientWithMonthlyVisitsResponse(
            name=client.name, visits=monthly_visits
        )
