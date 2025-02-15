from src.database.repositories.client_repository import ClientRepository
from src.database.repositories.coach_repository import CoachRepository
from src.database.repositories.visits_repository import VisitsRepository
from src.events.abc import AbstractSubject
from src.schemas.payload.visit.base import VisitBasePayloadWithNames
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.create_visit_service.abc import AbstractCreateVisitsService
from src.utils.get_entity import get_entity


class RepositoryCreateVisitsService(AbstractCreateVisitsService):
    def __init__(
        self,
        client_repository: ClientRepository,
        coach_repository: CoachRepository,
        visits_repository: VisitsRepository,
        subject: AbstractSubject[VisitBaseResponse] | None = None,
    ):
        self._client_repository = client_repository
        self._coach_repository = coach_repository
        self._visits_repository = visits_repository
        self._subject = subject

    async def create_visit(
        self, payload: VisitBasePayloadWithNames
    ) -> VisitBaseResponse:

        client = await get_entity(
            repository=self._client_repository,
            name=payload.client_name,
            entity_name="Client",
        )

        coach = await get_entity(
            repository=self._coach_repository,
            name=payload.coach_name,
            entity_name="Coach",
        )

        visit = await self._visits_repository.create(
            client_id=client.id,
            coach_id=coach.id,
            visit_datetime=payload.visit_datetime,
            training_type=payload.training_type,
        )

        created_visit = VisitBaseResponse.model_validate(visit)
        if self._subject is not None:
            await self._subject.update(created_visit)

        return created_visit
