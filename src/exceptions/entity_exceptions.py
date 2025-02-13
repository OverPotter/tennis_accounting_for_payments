from typing import Any


class EntityException(Exception):
    def __init__(self, key: str, value: Any, entity_name: str | None = None):
        self.key = key
        self.value = value
        self.entity_name = entity_name or "Entity"

    def __str__(self):
        return f"Error in {self.entity_name}: Field '{self.key}' with value '{self.value}' caused an issue."

    def __repr__(self):
        return f"EntityException(key={self.key!r}, value={self.value!r}, entity_name={self.entity_name!r})"

    def details(self):
        return f"Field: {self.key}, Value: {self.value}, Entity: {self.entity_name}."


class EntityAlreadyExistException(EntityException):
    def __init__(self, key: str, value: Any, entity_name: str | None = None):
        super().__init__(key, value, entity_name)
        self.message = (
            f"{self.entity_name} with {self.key} = {self.value} already exists."
        )

    def __str__(self):
        return self.message


class EntityDoesntExistException(EntityException):
    def __init__(self, key: str, value: Any, entity_name: str | None = None):
        super().__init__(key, value, entity_name)
        self.message = (
            f"{self.entity_name} with {self.key} = {self.value} doesn't exist."
        )

    def __str__(self):
        return self.message
