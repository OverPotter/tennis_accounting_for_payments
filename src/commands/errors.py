import sentry_sdk
from aiogram import Router
from aiogram.types import Update

from src.services.logging_service.logging_service import logger_factory

router = Router()
logger = logger_factory()


@router.errors()
async def global_error_handler(update: Update, exception: Exception):
    logger.exception(f"Произошла ошибка: {exception}")
    sentry_sdk.capture_exception(exception)
    return True
