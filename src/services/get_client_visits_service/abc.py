from abc import ABC, abstractmethod

from src.schemas.response.visit.base import VisitBaseResponse


class AbstractGetClientVisitsService(ABC):
    @abstractmethod
    async def get_all_client_visits_up_to_current_month(
        self, client_id: int, coach_name: str | None = None
    ) -> int: ...

    @abstractmethod
    async def get_monthly_client_visits(
        self, client_id: int, coach_name: str | None = None
    ) -> tuple[int, list[VisitBaseResponse]]: ...
