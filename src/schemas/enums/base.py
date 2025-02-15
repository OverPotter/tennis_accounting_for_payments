from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def from_value(cls, value: str):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(
            f"No matching enum member in {cls.__name__} for value: {value}. Enum members are: {', '.join([m.name for m in cls])}"
        )

    @classmethod
    def get_allowed_values(cls):
        return ", ".join([member.value for member in cls])
