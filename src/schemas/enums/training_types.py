from src.schemas.enums.base import BaseEnum

training_type_str_attribute_to_value = {
    "INDIVIDUAL_TRAINING": "индив",
    "SPLIT_TRAINING": "сплит",
    "GROUP_TRAINING": "группа",
}


class TrainingTypesEnum(BaseEnum):
    INDIVIDUAL_TRAINING = "индив"
    SPLIT_TRAINING = "сплит"
    GROUP_TRAINING = "группа"
