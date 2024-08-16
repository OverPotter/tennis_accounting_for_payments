from abc import ABC, abstractmethod

from src.schemas.enums.training_types import TrainingTypesEnum


class AbstractCreateVisitsService(ABC):
    @abstractmethod
    async def create_visits(
        self,
        client_name: str,
        visit_datetime: str,
        training_type: TrainingTypesEnum,
    ) -> bool: ...
