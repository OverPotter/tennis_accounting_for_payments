from typing import Dict, Type

from sqlalchemy.exc import OperationalError

from src.exceptions.access_control_exceptions import (
    RolePermissionError,
    UserNotRegisteredError,
)
from src.exceptions.entity_exceptions import (
    EntityAlreadyExistException,
    EntityDoesntExistException,
)
from src.exceptions.validation_exceptions import (
    InvalidAmountError,
    InvalidNameError,
    InvalidPaymentDataException,
    InvalidPaymentDateError,
    InvalidSpecializationError,
    InvalidTrainingTypeError,
    InvalidVisitDataException,
    InvalidVisitDatetimeError,
)
from src.schemas.enums.specializations import SpecializationEnum
from src.schemas.enums.training_types import TrainingTypesEnum

ERROR_MAP: Dict[Type[Exception], str] = {
    InvalidAmountError: "Введена некорректная сумма. Убедитесь, что сумма является числом.",
    InvalidNameError: "Введено некорректное имя. Имя должно состоять из имени и фамилии, содержащих только буквы латинского или русского алфавита.",
    InvalidPaymentDateError: "Неверный формат даты оплаты. Используйте формат DD.MM.YYYY.",
    InvalidTrainingTypeError: f"Неверный тип тренировки. Допустимые значения: {TrainingTypesEnum.get_allowed_values()}.",
    InvalidSpecializationError: f"Неверная специализация. Допустимые значения: {SpecializationEnum.get_allowed_values()}.",
    InvalidVisitDatetimeError: "Неверный формат даты и времени посещения. Используйте формат DD.MM.YYYY HH:MM.",
    InvalidVisitDataException: "Некорректные данные о посещении. Проверьте правильность заполнения информации.",
    InvalidPaymentDataException: "Некорректные данные об оплате. Проверьте правильность заполнения информации.",
    EntityAlreadyExistException: "Такой объект уже существует.",
    EntityDoesntExistException: "Запрашиваемый объект не найден.",
    IndexError: "Не хватает данных для обработки запроса. Проверьте ввод.",
    OperationalError: "Ошибка соединения с базой данных. Попробуйте позже или сообщите администратору.",
    UserNotRegisteredError: "Пользователь с таким ID не зарегистрирован в системе админов.",
    RolePermissionError: "Отказ в доступе: у пользователя нет прав для выполнения этой операции.",
}
