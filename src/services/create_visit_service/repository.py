from src.database.repositories.client_repository import ClientRepository
from src.database.repositories.coach_repository import CoachRepository
from src.database.repositories.visits_repository import VisitsRepository
from src.events.abc import AbstractSubject
from src.schemas.payload.visit.base import VisitBasePayloadWithNames
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.create_visit_service.abc import AbstractCreateVisitsService


class RepositoryCreateVisitsService(AbstractCreateVisitsService):
    def __init__(
        self,
        client_repository: ClientRepository,
        coach_repository: CoachRepository,
        visits_repository: VisitsRepository,
    ):
        self._client_repository = client_repository
        self._coach_repository = coach_repository
        self._visits_repository = visits_repository

    async def create_visit(
        self,
        payload: VisitBasePayloadWithNames,
        subject: AbstractSubject[VisitBaseResponse] | None = None,
    ) -> VisitBaseResponse:

        client = await self._client_repository.get_or_raise_by_name(
            name=payload.client_name
        )

        coach = await self._coach_repository.get_or_raise_by_name(
            name=payload.coach_name
        )

        visit = await self._visits_repository.create(
            client_id=client.id,
            coach_id=coach.id,
            visit_datetime=payload.visit_datetime,
            training_type=payload.training_type,
        )

        created_visit = VisitBaseResponse.model_validate(visit)
        if subject is not None:
            await subject.update(created_visit)

        return created_visit
