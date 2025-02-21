from src.database.repositories.coach_repository import CoachRepository
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
        await self._coach_repository.check_coach_does_not_exist_by_name(
            name=payload.name
        )
        coach = await self._coach_repository.create(**payload.model_dump())

        return CoachBaseResponse.model_validate(coach)
