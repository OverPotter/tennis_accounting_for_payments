from abc import ABC, abstractmethod

from src.schemas.payload.visit.base import VisitBasePayloadWithNames
from src.schemas.response.visit.base import VisitBaseResponse


class AbstractCreateVisitsService(ABC):
    @abstractmethod
    async def create_visit(
        self, payload: VisitBasePayloadWithNames
    ) -> VisitBaseResponse: ...
