import datetime


def get_first_day_of_current_month() -> datetime.date:
    return datetime.date.today().replace(day=1)
