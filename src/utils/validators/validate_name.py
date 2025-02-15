from src.constants.regular_expressions import NAME_PATTERN
from src.exceptions.validation_exceptions import InvalidNameError


def validate_full_name(full_name: str) -> str:
    if not NAME_PATTERN.match(full_name.strip()):
        raise InvalidNameError(full_name)

    return full_name.strip()
