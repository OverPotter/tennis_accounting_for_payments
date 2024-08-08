from src.schemas.enums.base import BaseEnum


class TrainingTypeEnum(BaseEnum):
    INDIVIDUAL_TRAINING = "индив"
    SPLIT_TRAINING = "сплит"
    GROUP_TRAINING = "группа"
