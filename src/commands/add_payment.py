from aiogram import Router, types
from aiogram.filters import Command

from src.database.repositories.manager import orm_repository_manager_factory

router = Router()


@router.message(Command("add_payment"))
async def add_payment(message: types.Message):
    repository_manager = orm_repository_manager_factory()
    async with repository_manager:
        ...
