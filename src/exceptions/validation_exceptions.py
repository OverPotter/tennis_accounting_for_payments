from src.schemas.enums.specializations import SpecializationEnum
from src.schemas.enums.training_types import TrainingTypesEnum


class ValidationError(Exception):
    def __init__(self, message: str, *args):
        super().__init__(message, *args)
        self.message = message

    def __str__(self):
        return self.message


class InvalidAmountError(ValidationError):
    def __init__(self, amount: str):
        message = f"The amount format is incorrect. The amount must be a number: {amount}"
        super().__init__(message)
        self.amount = amount


class InvalidNameError(ValidationError):
    def __init__(self, invalid_part: str):
        message = f"Invalid character(s) in name part: {invalid_part}. Only letters from English or Russian alphabets are allowed."
        super().__init__(message)
        self.invalid_part = invalid_part


class InvalidPaymentDateError(ValidationError):
    def __init__(self, date: str):
        message = (
            f"The date format is incorrect: {date}. Use the DD.MM.YYYY format."
        )
        super().__init__(message)
        self.date = date


class InvalidTrainingTypeError(ValidationError):
    def __init__(self, training_type: str):
        message = f"The training type '{training_type}' is invalid. Valid types are: {TrainingTypesEnum.get_allowed_values()}."
        super().__init__(message)
        self.training_type = training_type


class InvalidSpecializationError(ValidationError):
    def __init__(self, specialization: str):
        message = f"The specialization '{specialization}' is invalid. Valid types are: {SpecializationEnum.get_allowed_values()}."
        super().__init__(message)
        self.specialization = specialization


class InvalidVisitDatetimeError(ValidationError):
    def __init__(self, visit_datetime: str):
        message = f"The date format is incorrect: {visit_datetime}. Use the DD.MM.YYYY HH:MM format."
        super().__init__(message)
        self.visit_datetime = visit_datetime
