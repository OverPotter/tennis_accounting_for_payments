from datetime import date, datetime

from src.constants.regular_expressions import DATE_PATTERN
from src.exceptions.validation_exceptions import InvalidPaymentDateError


def validate_payment_date(payment_date: str) -> date:
    try:
        return datetime.strptime(payment_date, DATE_PATTERN).date()
    except ValueError:
        raise InvalidPaymentDateError(payment_date)
