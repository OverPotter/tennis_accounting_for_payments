from datetime import datetime


def validate_and_extract_visit_datetime(parts: list[str]) -> str:
    visit_datetime = f"{parts[2]} {parts[3]}"
    try:
        dt = datetime.strptime(visit_datetime, "%d.%m.%Y %H:%M")
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise ValueError(
            f"The date format is incorrect: {visit_datetime}. Use the DD.MM.YYYY HH:MM format."
        )
