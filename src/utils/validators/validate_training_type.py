from src.exceptions.validation_exceptions import InvalidTrainingTypeError
from src.schemas.enums.training_types import TrainingTypesEnum


def validate_training_type(training_type: str) -> TrainingTypesEnum:
    try:
        return TrainingTypesEnum.from_value(training_type)
    except ValueError:
        raise InvalidTrainingTypeError(training_type)
