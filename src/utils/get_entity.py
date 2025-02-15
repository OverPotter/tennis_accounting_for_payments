from src.database.repositories.absctract_repository import (
    MODEL_TYPE,
    AbstractRepository,
)
from src.exceptions.entity_exceptions import EntityDoesntExistException


async def get_entity(
    repository: AbstractRepository, name: str, entity_name: str
) -> MODEL_TYPE:
    entity = await repository.get(name=name)
    if not entity:
        raise EntityDoesntExistException(
            key="name", value=name, entity_name=entity_name
        )
    return entity
