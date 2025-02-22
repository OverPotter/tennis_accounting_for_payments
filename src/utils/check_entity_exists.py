from typing import Any, Type

from src.database.models import ClientModel
from src.database.models.models import CoachModel
from src.exceptions.entity_exceptions import (
    EntityAlreadyExistException,
    EntityDoesntExistException,
)


def check_entity_exists_by_name(
    data: Any, model: Type[ClientModel | CoachModel], value: str
) -> None:
    if not data:
        raise EntityDoesntExistException(
            key=model.name.key,
            value=value,
            entity_name=model.__tablename__,
        )


def check_entity_does_not_exist_by_name(
    data: Any, model: Type[ClientModel | CoachModel], value: str
) -> None:
    if data:
        raise EntityAlreadyExistException(
            key=model.name.key,
            value=value,
            entity_name=model.__tablename__,
        )
