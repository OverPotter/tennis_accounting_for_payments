from src.constants import PRICE_LIST
from src.schemas.enums.training_types import TrainingTypesEnum


def get_training_type_by_amount(
    amount: float,
) -> tuple[int, TrainingTypesEnum] | tuple[str, None]:
    return PRICE_LIST.get(amount, ("InvalidPrice", None))
