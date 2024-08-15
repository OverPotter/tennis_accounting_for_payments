def validate_and_extract_amount(parts: list[str]) -> float:
    try:
        return float(parts[2])
    except ValueError:
        raise ValueError(
            f"The amount format is incorrect. The amount must be a number: {parts[2]}."
        )
