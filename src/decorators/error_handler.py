from functools import wraps

from sqlalchemy.exc import OperationalError

from src.exceptions.entity_exceptions import (
    EntityAlreadyExistException,
    EntityDoesntExistException,
)
from src.services.logging_service.logging_service import logger_factory

logger = logger_factory()


def error_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except EntityAlreadyExistException as e:
            logger.error(f"Error: {e}.")
            message = kwargs.get("message") or args[0]
            await message.answer(f"Ошибка: {e}.")

        except EntityDoesntExistException as e:
            logger.error(f"Error: {e}.")
            message = kwargs.get("message") or args[0]
            await message.answer(f"Ошибка: {e}.")

        except ValueError as e:
            logger.error(f"Invalid data: {e}.")
            message = kwargs.get("message") or args[0]
            await message.answer(f"Данные не валидны: {e}.")

        except IndexError as e:
            logger.error(f"Problems with input data parsing: {e}.")
            message = kwargs.get("message") or args[0]
            await message.answer(
                "Проблемы с анализом входных данных, возможно вы указали не все данные."
            )

        except OperationalError as e:
            logger.error(f"Database error: {e}.")
            message = kwargs.get("message") or args[0]
            await message.answer(
                "Проблемы с базой данных. Сообщите администратору."
            )

        except Exception as e:
            logger.exception(f"Unexpected error: {e}.")
            message = kwargs.get("message") or args[0]
            await message.answer(
                "Произошла непредвиденная ошибка. Сообщите администратору."
            )

    return wrapper
