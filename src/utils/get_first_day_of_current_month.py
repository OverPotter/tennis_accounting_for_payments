import datetime


def get_first_day_of_current_month() -> datetime.date:
    """
    Get the first day of the current month
    to get data on visits up to that time.
    """
    return datetime.date.today().replace(day=1)
