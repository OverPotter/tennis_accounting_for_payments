import calendar
from datetime import datetime

from babel.dates import format_date

from src.schemas.response.month.base import MonthDetailsBaseResponse


def _get_current_year_and_month() -> tuple[int, int]:
    current_time = datetime.now()
    return current_time.year, current_time.month


def _get_days_in_month(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]


def _get_month_name_in_russian(year: int, month: int) -> str:
    current_time = datetime(year, month, 1)
    return format_date(current_time, "LLLL", locale="ru").capitalize()


def get_current_month_details() -> MonthDetailsBaseResponse:
    year, month = _get_current_year_and_month()
    days = _get_days_in_month(year, month)
    month_name = _get_month_name_in_russian(year, month)

    return MonthDetailsBaseResponse(
        total_days=days,
        name=month_name,
        year=year,
    )
