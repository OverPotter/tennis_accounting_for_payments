from src.database.repositories.user_repository import ClientRepository
from src.database.repositories.visits_repository import VisitsRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException
from src.schemas.enums.training_types import TrainingTypesEnum
from src.services.create_visits_service.abc import AbstractCreateVisitsService


class RepositoryCreateVisitsService(AbstractCreateVisitsService):
    def __init__(
        self,
        client_repository: ClientRepository,
        visits_repository: VisitsRepository,
    ):
        self._client_repository = client_repository
        self._visits_repository = visits_repository

    async def create_visits(
        self,
        client_name: str,
        visit_datetime: str,
        training_type: TrainingTypesEnum,
    ) -> bool:
        client = await self._client_repository.get(name=client_name)
        if not client:
            raise EntityDoesntExistException(
                key="name",
                value=client_name,
                entity_name="client",
            )

        visits = await self._visits_repository.create(
            client_id=client.id,
            visit_datetime=visit_datetime,
            training_type=training_type,
        )
        return bool(visits)
