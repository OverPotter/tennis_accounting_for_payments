from datetime import datetime

from src.constants.regular_expressions import DATETIME_PATTERN
from src.exceptions.validation_exceptions import InvalidVisitDatetimeError


def validate_visit_datetime(date_and_time: str) -> datetime:
    try:
        return datetime.strptime(date_and_time, DATETIME_PATTERN)
    except ValueError:
        raise InvalidVisitDatetimeError(date_and_time)
