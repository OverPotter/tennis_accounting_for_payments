from abc import ABC, abstractmethod

from src.schemas.response.payment.base import PaymentBaseResponse


class AbstractGetPaidClientTrainingService(ABC):
    @abstractmethod
    async def get_all_client_paid_training_up_to_current_month(
        self, client_id: int, coach_name: str | None = None
    ) -> int: ...

    @abstractmethod
    async def get_monthly_paid_client_trainings(
        self, client_id: int, coach_name: str | None = None
    ) -> list[PaymentBaseResponse]: ...
