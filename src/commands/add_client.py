from aiogram import Router, types
from aiogram.filters import Command

from src.database.repositories.manager import orm_repository_manager_factory
from src.handlers.add_client.add_client import AddClientCommandHandler
from src.services.create_client_service.repository import (
    RepositoryCreateClientService,
)

router = Router()


@router.message(Command("add_client"))
async def add_client(message: types.Message):
    repository_manager = orm_repository_manager_factory()
    async with repository_manager:
        handler = AddClientCommandHandler(
            create_client_service=RepositoryCreateClientService(
                client_repository=repository_manager.get_client_repository()
            )
        )
    await handler.handle(message=message)