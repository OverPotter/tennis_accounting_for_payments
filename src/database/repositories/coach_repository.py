from src.database.models.models import CoachModel
from src.database.repositories.absctract_repository import AbstractRepository
from src.exceptions.entity_exceptions import EntityDoesntExistException


class CoachRepository(AbstractRepository[CoachModel]):
    _model = CoachModel

    async def get_or_raise_by_name(self, name: str) -> _model:
        entity = await self.get(name=name)
        if not entity:
            raise EntityDoesntExistException(
                key=self._model.name.key,
                value=name,
                entity_name=self._model.__tablename__,
            )
        return entity
