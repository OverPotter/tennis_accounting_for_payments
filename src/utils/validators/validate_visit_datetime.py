from datetime import datetime

from src.constants.regular_expressions import DATETIME_PATTERN
from src.exceptions.validation_exceptions import InvalidVisitDatetimeError


def validate_and_extract_visit_datetime(parts: list[str]) -> datetime:
    visit_datetime = f"{parts[2]} {parts[3]}"
    try:
        return datetime.strptime(visit_datetime, DATETIME_PATTERN)
    except ValueError:
        raise InvalidVisitDatetimeError(visit_datetime)
