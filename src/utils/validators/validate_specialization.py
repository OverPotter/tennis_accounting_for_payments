from src.exceptions.validation_exceptions import InvalidSpecializationError
from src.schemas.enums.specializations import SpecializationEnum


def validate_specialization(
    specialization: str,
) -> SpecializationEnum:
    try:
        return SpecializationEnum.from_value(specialization)
    except ValueError:
        raise InvalidSpecializationError(specialization)
