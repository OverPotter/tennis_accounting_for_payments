from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def from_value(cls, value: str):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"No matching {__class__} member for value: {value}")
