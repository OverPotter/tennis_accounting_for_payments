import logging

from src.database.repositories.user_repository import UserRepository
from src.services.create_client_service.abc import AbstractCreateClientService


class RepositoryCreateClientService(AbstractCreateClientService):
    def __init__(
        self,
        client_repository: UserRepository,
    ):
        self._client_repository = client_repository

    async def create_user(self, user_name: str) -> bool:
        is_create = await self._client_repository.get(name=user_name)
        if is_create:
            logging.info(f"{self.__class__}: User already exists.")
            return True

        client = await self._client_repository.create(name=user_name)

        logging.info(f"{self.__class__}: User created.")
        return bool(client)
