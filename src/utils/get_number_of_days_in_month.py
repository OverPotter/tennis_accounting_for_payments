import calendar
import locale
from datetime import datetime

from babel.dates import format_date


def get_number_of_days_in_month() -> tuple[int, str, int]:
    current_time = datetime.now()
    current_year = current_time.year
    current_month = current_time.month

    number_days_of_in_month = calendar.monthrange(current_year, current_month)[1]

    locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")
    current_month_name = format_date(current_time, "LLLL", locale="ru").capitalize()

    return number_days_of_in_month, current_month_name, current_year
