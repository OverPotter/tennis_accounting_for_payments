from functools import wraps
from typing import Any, Awaitable, Callable

import sentry_sdk
from aiogram import types

from src.constants.error_map import ERROR_MAP
from src.services.logging_service.logging_service import logger_factory

logger = logger_factory()


async def handle_exception(e: Exception, message: types.Message) -> None:
    error_message = ERROR_MAP.get(
        type(e),
        "Произошла непредвиденная ошибка. Пожалуйста, сообщите администратору.",
    )

    if type(e) in ERROR_MAP:
        logger.warning(f"{error_message}: {e}")
    else:
        logger.exception(f"Unexpected error: {e}")

    sentry_sdk.capture_exception(e)
    await message.answer(error_message)


def error_handler(
    func: Callable[..., Awaitable[Any]]
) -> Callable[..., Awaitable[Any]]:
    @wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            message = kwargs.get("message") or args[0]
            await handle_exception(e, message)

    return wrapper
