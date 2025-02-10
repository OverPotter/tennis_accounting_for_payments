from pathlib import Path

from src.schemas.enums.training_types import TrainingTypesEnum

# todo: create new file for every constants set
TMP_DIR = Path(__file__).resolve().parents[0] / "tmp"
ENV_PATH = Path(__file__).resolve().parents[1] / "docker" / "backend" / ".env"

XLSX_FILE_NAME = "Таблица_Посещений"
XLSX_SUB_HEADERS = [
    "ФИО",
    "Остаточный переход количество",
    "Сумма оплаты",
    "Количество тренировок",
    "Дата оплаты",
]
XLSX_LAST_SUB_HEADER = "Количество оставшихся тренировок"

PRICE_LIST = {
    45.0: (1, TrainingTypesEnum.GROUP_TRAINING),
    160.0: (4, TrainingTypesEnum.GROUP_TRAINING),
    310.0: (8, TrainingTypesEnum.GROUP_TRAINING),
    55.0: (1, TrainingTypesEnum.SPLIT_TRAINING),
    110.0: (1, TrainingTypesEnum.INDIVIDUAL_TRAINING),
}

OFFSET_AFTER_HEADERS_FOR_XLSX = 3
OFFSET_BETWEEN_CLIENTS = 0

POSITIVE_TRAINING_COUNT = "A0F49A"
NEGATIVE_TRAINING_COUNT = "FF92C2"
NEUTRAL_TRAINING_COUNT = "D9D9D9"

TABLE_BACKGROUND = "DBF9CD"
HEADER_BACKGROUND = "9AF4A9"
