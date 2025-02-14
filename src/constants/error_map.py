from typing import Dict, Type

from sqlalchemy.exc import OperationalError

from src.exceptions.entity_exceptions import (
    EntityAlreadyExistException,
    EntityDoesntExistException,
)

ERROR_MAP: Dict[Type[Exception], str] = {
    EntityAlreadyExistException: "Такой объект уже существует.",
    EntityDoesntExistException: "Запрашиваемый объект не найден.",
    ValueError: "Введены некорректные данные. Проверьте их и попробуйте снова.",
    IndexError: "Не хватает данных для обработки запроса. Проверьте ввод.",
    OperationalError: "Ошибка соединения с базой данных. Попробуйте позже или сообщите администратору.",
}
