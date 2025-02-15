from src.database.repositories.coach_repository import CoachRepository
from src.exceptions.entity_exceptions import EntityAlreadyExistException
from src.schemas.payload.coach.base import CoachBasePayload
from src.schemas.response.coach.base import CoachBaseResponse
from src.services.create_coach_service.abc import AbstractCreateCoachService


class RepositoryCreateCoachService(AbstractCreateCoachService):
    def __init__(
        self,
        coach_repository: CoachRepository,
    ):
        self._coach_repository = coach_repository

    async def create_coach(
        self, payload: CoachBasePayload
    ) -> CoachBaseResponse:
        is_coach_exist = await self._coach_repository.get(name=payload.name)
        if is_coach_exist:
            raise EntityAlreadyExistException(
                key="Name",
                value=payload.name,
                entity_name="Coach",
            )

        coach = await self._coach_repository.create(**payload.dict())

        return CoachBaseResponse.model_validate(coach)
