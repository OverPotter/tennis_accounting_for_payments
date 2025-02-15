from typing import Any, Awaitable, Callable, Dict

import sentry_sdk
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from src.services.logging_service.logging_service import logger_factory

logger = logger_factory()


class ErrorHandlerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        try:
            return await handler(event, data)

        except Exception as e:
            logger.exception(f"Произошла ошибка: {e}")
            sentry_sdk.capture_exception(e)

            raise e
