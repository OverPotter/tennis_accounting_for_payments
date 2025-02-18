from functools import wraps

from aiogram import types

from src.database.repositories.manager import orm_repository_manager_factory
from src.decorators.error_handler import handle_exception
from src.exceptions.access_control_exceptions import (
    RolePermissionError,
    UserNotRegisteredError,
)
from src.schemas.enums.admin_roles import AdminRoleEnum


def checking_permissions(allowed_roles: list[AdminRoleEnum]):
    def decorator(func):
        @wraps(func)
        async def wrapper(message: types.Message):
            repository_manager = orm_repository_manager_factory()
            async with repository_manager:
                admin_repository = repository_manager.get_admin_repository()
                user_id = message.from_user.id

                try:
                    admin = await admin_repository.get(tg_id=user_id)

                    if not admin:
                        raise UserNotRegisteredError(
                            user_id=user_id,
                            username=message.from_user.username,
                            first_name=message.from_user.first_name,
                            last_name=message.from_user.last_name,
                        )

                    if admin.role not in allowed_roles:
                        raise RolePermissionError(
                            user_id=user_id,
                            username=message.from_user.username,
                            first_name=message.from_user.first_name,
                            last_name=message.from_user.last_name,
                            role=admin.role.value,
                        )

                    return await func(message)

                except (UserNotRegisteredError, RolePermissionError) as e:
                    await handle_exception(e, message)

        return wrapper

    return decorator
