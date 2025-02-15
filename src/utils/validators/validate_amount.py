from src.exceptions.validation_exceptions import InvalidAmountError


def validate_amount(amount: str) -> float:
    try:
        return float(amount)
    except ValueError:
        raise InvalidAmountError(amount)
