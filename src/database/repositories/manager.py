from sqlalchemy.ext.asyncio import AsyncSession

from src.database.repositories.abstract_manager import AbstractRepositoryManager
from src.database.repositories.admin_repository import AdminRepository
from src.database.repositories.client_repository import ClientRepository
from src.database.repositories.coach_repository import CoachRepository
from src.database.repositories.number_of_tennis_training_available_repository import (
    NumberOfTennisTrainingAvailableRepository,
)
from src.database.repositories.payment_repository import PaymentRepository
from src.database.repositories.visits_repository import VisitsRepository
from src.db_manager import session_factory


class OrmRepositoryManager(AbstractRepositoryManager):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

    async def close(self) -> None:
        await self._session.close()

    def get_client_repository(self) -> ClientRepository:
        return ClientRepository(self._session)

    def get_payment_repository(self) -> PaymentRepository:
        return PaymentRepository(self._session)

    def get_admin_repository(self) -> AdminRepository:
        return AdminRepository(self._session)

    def get_visits_repository(self) -> VisitsRepository:
        return VisitsRepository(self._session)

    def get_number_of_tennis_training_available_repository(
        self,
    ) -> NumberOfTennisTrainingAvailableRepository:
        return NumberOfTennisTrainingAvailableRepository(self._session)

    def get_coach_repository(self) -> CoachRepository:
        return CoachRepository(self._session)


def orm_repository_manager_factory() -> OrmRepositoryManager:
    return OrmRepositoryManager(session_factory())
