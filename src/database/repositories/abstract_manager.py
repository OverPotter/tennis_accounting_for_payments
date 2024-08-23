from abc import ABC, abstractmethod
from inspect import Traceback
from typing import Type

from src.database.repositories.admin_repository import AdminRepository
from src.database.repositories.client_repository import ClientRepository
from src.database.repositories.monthly_visits_repository import (
    MonthlyVisitsRepository,
)
from src.database.repositories.number_of_tennis_training_available_repository import (
    NumberOfTennisTrainingAvailableRepository,
)
from src.database.repositories.payment_repository import PaymentRepository
from src.database.repositories.visits_repository import VisitsRepository


class AbstractRepositoryManager(ABC):

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...

    @abstractmethod
    async def close(self) -> None: ...

    async def __aenter__(self):
        pass

    async def __aexit__(
        self, exc_type: Type[Exception], exc_val: Exception, exc_tb: Traceback
    ) -> None:
        if exc_val:
            await self.rollback()
        else:
            await self.commit()
        await self.close()

    @abstractmethod
    def get_client_repository(self) -> ClientRepository: ...

    @abstractmethod
    def get_payment_repository(self) -> PaymentRepository: ...

    @abstractmethod
    def get_visits_repository(self) -> VisitsRepository: ...

    @abstractmethod
    def get_admin_repository(self) -> AdminRepository: ...

    @abstractmethod
    def get_number_of_tennis_training_available_repository(
        self,
    ) -> NumberOfTennisTrainingAvailableRepository: ...

    @abstractmethod
    def get_monthly_visits_repository(self) -> MonthlyVisitsRepository: ...
