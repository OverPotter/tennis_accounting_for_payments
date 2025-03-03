from typing import Callable

from sqlalchemy import and_, select, update

from src.database.models import NumberOfTennisTrainingAvailableModel
from src.database.repositories.absctract_repository import AbstractRepository
from src.schemas.enums.training_types import TrainingTypesEnum


class NumberOfTennisTrainingAvailableRepository(
    AbstractRepository[NumberOfTennisTrainingAvailableModel]
):
    _model = NumberOfTennisTrainingAvailableModel

    async def update(
        self,
        client_id: int,
        coach_id: int,
        training_type: TrainingTypesEnum,
        **kwargs
    ) -> Callable[[], int]:
        query = (
            update(NumberOfTennisTrainingAvailableModel)
            .where(
                and_(
                    NumberOfTennisTrainingAvailableModel.client_id == client_id,
                    NumberOfTennisTrainingAvailableModel.coach_id == coach_id,
                    NumberOfTennisTrainingAvailableModel.training_type
                    == training_type,
                )
            )
            .values(**kwargs)
        )
        result = await self._session.execute(query)
        return result.rowcount

    async def get_number_by_constraint_pk(
        self, client_id: int, coach_id: int, training_type: TrainingTypesEnum
    ) -> _model | None:
        query = select(NumberOfTennisTrainingAvailableModel).where(
            and_(
                NumberOfTennisTrainingAvailableModel.client_id == client_id,
                NumberOfTennisTrainingAvailableModel.coach_id == coach_id,
                NumberOfTennisTrainingAvailableModel.training_type
                == training_type,
            )
        )
        result = await self._session.execute(query)
        return result.scalar_one_or_none()
