from datetime import date, datetime

from src.constants.regular_expressions import DATE_PATTERN
from src.exceptions.validation_exceptions import InvalidPaymentDateError


def validate_and_extract_payment_date(parts: list[str]) -> date:
    if len(parts) == 4 and parts[3].strip():
        payment_date = parts[3].strip()
        try:
            return datetime.strptime(payment_date, DATE_PATTERN).date()
        except ValueError:
            raise InvalidPaymentDateError(payment_date)
    else:
        return datetime.now().date()
