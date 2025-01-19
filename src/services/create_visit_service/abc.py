from abc import ABC, abstractmethod

from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.response.visit.base import VisitBaseResponse


class AbstractCreateVisitsService(ABC):
    @abstractmethod
    async def create_visit(
        self,
        client_name: str,
        visit_datetime: str,
        training_type: TrainingTypesEnum,
    ) -> VisitBaseResponse: ...
