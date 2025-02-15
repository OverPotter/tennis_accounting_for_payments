import re

NAME_PATTERN = re.compile(r"^[a-zA-Zа-яА-Я]+$")
DATE_PATTERN = "%d.%m.%Y"
DATETIME_PATTERN = "%d.%m.%Y %H:%M"
