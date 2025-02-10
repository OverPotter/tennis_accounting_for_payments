from datetime import datetime

from pydantic import TypeAdapter

from src.database.repositories.client_repository import ClientRepository
from src.database.repositories.visits_repository import VisitsRepository
from src.events.abc import AbstractSubject
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.response.visit.base import VisitBaseResponse
from src.services.create_visit_service.abc import AbstractCreateVisitsService


class RepositoryCreateVisitsService(AbstractCreateVisitsService):
    def __init__(
        self,
        client_repository: ClientRepository,
        visits_repository: VisitsRepository,
        subject: AbstractSubject[VisitBaseResponse] | None = None,
    ):
        self._client_repository = client_repository
        self._visits_repository = visits_repository
        self._subject = subject

    async def create_visit(
        self,
        client_name: str,
        visit_datetime: datetime,
        training_type: TrainingTypesEnum,
    ) -> VisitBaseResponse:

        client = await self._client_repository.get(name=client_name)
        if not client:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        visit = await self._visits_repository.create(
            client_id=client.id,
            visit_datetime=visit_datetime,
            training_type=training_type,
        )
        created_visit = TypeAdapter(VisitBaseResponse).validate_python(visit)  # type: ignore
        if self._subject is not None:
            await self._subject.update(created_visit)

        return created_visit
