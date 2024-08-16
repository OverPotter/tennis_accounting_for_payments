from abc import ABC, abstractmethod

from aiogram import types

from src.services.logging_service.logging_service import logger_factory


class BaseCommandHandler(ABC):
    def __init__(self):
        self._logger = logger_factory()

    @abstractmethod
    def handle(self, message: types.Message) -> None: ...
