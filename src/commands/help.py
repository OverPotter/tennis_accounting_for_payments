from aiogram import Router, types
from aiogram.filters import Command

from src.handlers.help.help_handler import HelpCommandHandler

router = Router()


@router.message(Command("help"))
async def send_help(message: types.Message):
    handler = HelpCommandHandler()
    await handler.handle(message=message)
