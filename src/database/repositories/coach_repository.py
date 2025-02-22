from src.database.models.models import CoachModel
from src.database.repositories.absctract_repository import AbstractRepository
from src.utils.check_entity_exists import (
    check_entity_does_not_exist_by_name,
    check_entity_exists_by_name,
)


class CoachRepository(AbstractRepository[CoachModel]):
    _model = CoachModel

    async def check_coach_does_not_exist_by_name(self, name: str) -> None:
        coach_data = await self.get(name=name)
        check_entity_does_not_exist_by_name(
            data=coach_data, model=self._model, value=name
        )

    async def get_or_raise_by_name(self, name: str) -> _model:
        coach_data = await self.get(name=name)
        check_entity_exists_by_name(
            data=coach_data, model=self._model, value=name
        )

        return coach_data
