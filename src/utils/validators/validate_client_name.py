import re


def validate_and_extract_client_name(parts: list[str]) -> str:
    name_parts = parts[:2]
    name_pattern = re.compile(r"^[a-zA-Zа-яА-Я]+$")

    for part in name_parts:
        if not name_pattern.match(part):
            raise ValueError(
                f"Invalid character(s) in client name part: {part}. Only letters from English or Russian alphabets "
                f"are allowed."
            )

    return f"{parts[0]} {parts[1]}"
