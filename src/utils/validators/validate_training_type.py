from src.exceptions.validation_exceptions import InvalidTrainingTypeError
from src.schemas.enums.training_types import TrainingTypesEnum


def validate_and_extract_training_type(parts: list[str]) -> TrainingTypesEnum:
    training_type = parts[-1]
    try:
        return TrainingTypesEnum.from_value(training_type)
    except ValueError:
        raise InvalidTrainingTypeError(training_type)
