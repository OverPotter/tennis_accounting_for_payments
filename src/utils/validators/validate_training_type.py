from src.schemas.enums.training_types import TrainingTypesEnum


def validate_and_extract_training_type(parts: list[str]) -> TrainingTypesEnum:
    training_type = parts[-1]
    return TrainingTypesEnum.from_value(training_type)
