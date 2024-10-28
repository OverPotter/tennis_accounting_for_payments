from abc import ABC, abstractmethod

from src.schemas.response.visit.base import VisitBaseResponse


class AbstractGetClientVisitsService(ABC):
    @abstractmethod
    async def get_all_client_visits_up_to_current_month(
        self, client_id: int
    ) -> int: ...

    @abstractmethod
    async def get_monthly_client_visits(
        self, client_id: int
    ) -> tuple[int, list[VisitBaseResponse]]: ...
