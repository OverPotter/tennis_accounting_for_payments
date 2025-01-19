import datetime


def get_last_day_of_current_month(first_day: datetime.date) -> datetime.date:
    return (first_day + datetime.timedelta(days=32)).replace(
        day=1
    ) - datetime.timedelta(days=1)
