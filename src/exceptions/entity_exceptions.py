from typing import Any


class EntityException(Exception):
    def __init__(self, key: str, value: Any, entity_name: str | None = None):
        self.key = key
        self.value = value
        self.entity_name = entity_name

    def details(self):
        return f"Field: {self.key}, value: {self.value}, entity: {self.entity_name}"


class EntityAlreadyExistException(EntityException):
    pass


class EntityDoesntExistException(EntityException):
    pass


class VisitCreationException(EntityException):
    pass
