from abc import ABC, abstractmethod
from datetime import datetime

from src.schemas.enums.training_types import TrainingTypesEnum
from src.schemas.response.visit.base import VisitBaseResponse


class AbstractCreateVisitsService(ABC):
    @abstractmethod
    async def create_visit(
        self,
        client_name: str,
        visit_datetime: datetime,
        training_type: TrainingTypesEnum,
    ) -> VisitBaseResponse: ...
