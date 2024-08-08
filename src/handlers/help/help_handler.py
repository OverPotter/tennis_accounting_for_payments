import logging

from aiogram import types
from aiogram.exceptions import TelegramAPIError

from src.handlers.help.text import HELP_TEXT


class HelpCommandHandler:
    @staticmethod
    async def handle(message: types.Message):
        try:  # todo
            await message.answer(HELP_TEXT)
        except TelegramAPIError as e:
            logging.debug(f"Something wrong with connection: {e}")
