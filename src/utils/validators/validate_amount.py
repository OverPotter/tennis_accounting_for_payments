from src.exceptions.validation_exceptions import InvalidAmountError


def validate_and_extract_amount(parts: list[str]) -> float:
    try:
        return float(parts[2])
    except ValueError:
        raise InvalidAmountError(parts[2])
