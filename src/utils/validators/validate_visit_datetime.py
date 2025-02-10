from datetime import datetime


def validate_and_extract_visit_datetime(parts: list[str]) -> datetime:
    visit_datetime = f"{parts[2]} {parts[3]}"
    try:
        return datetime.strptime(visit_datetime, "%d.%m.%Y %H:%M")
    except ValueError:
        raise ValueError(
            f"The date format is incorrect: {visit_datetime}. Use the DD.MM.YYYY HH:MM format."
        )
