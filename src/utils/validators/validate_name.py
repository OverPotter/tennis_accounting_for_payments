from src.constants.regular_expressions import NAME_PATTERN
from src.exceptions.validation_exceptions import InvalidNameError


def validate_and_extract_name(parts: list[str]) -> str:
    name_parts = parts[:2]

    for part in name_parts:
        if not NAME_PATTERN.match(part):
            raise InvalidNameError(part)

    return f"{parts[0]} {parts[1]}"
