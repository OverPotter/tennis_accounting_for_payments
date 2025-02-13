from aiogram import types

from src.database.repositories.manager import orm_repository_manager_factory
from src.services.logging_service.logging_service import logger_factory


def checking_permissions(func):
    logger = logger_factory()

    async def wrapper(message: types.Message):
        repository_manager = orm_repository_manager_factory()
        async with repository_manager:
            admin_repository = repository_manager.get_admin_repository()

            user_id = message.from_user.id

            if await admin_repository.is_admin(tg_id=user_id):
                await func(message)
            else:
                logger.warning(
                    f"Unauthorized access attempt: user_id: {message.from_user.id}, tg_name: {message.from_user.username}, name: {message.from_user.first_name}, last_name: {message.from_user.last_name}"
                )
                await message.reply(
                    "У вас нет прав для выполнения этой команды."
                )

    return wrapper
