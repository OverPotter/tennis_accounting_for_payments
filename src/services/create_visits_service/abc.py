from abc import ABC, abstractmethod


class AbstractCreateVisitsService(ABC):
    @abstractmethod
    async def create_visits(
        self, client_name: str, visit_datetime: str, training_type: str
    ) -> bool: ...
