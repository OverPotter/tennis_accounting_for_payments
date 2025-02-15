from abc import ABC, abstractmethod

from src.schemas.payload.coach.base import CoachBasePayload
from src.schemas.response.coach.base import CoachBaseResponse


class AbstractCreateCoachService(ABC):
    @abstractmethod
    async def create_coach(
        self, payload: CoachBasePayload
    ) -> CoachBaseResponse: ...
