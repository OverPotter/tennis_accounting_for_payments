from datetime import date, datetime


def validate_and_extract_payment_date(parts: list[str]) -> date:
    if len(parts) == 4 and parts[3].strip():
        payment_date = parts[3].strip()
        try:
            return datetime.strptime(payment_date, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(
                f"The date format is incorrect: {payment_date}. Use the DD.MM.YYYY format."
            )
    else:
        return datetime.now().date()
