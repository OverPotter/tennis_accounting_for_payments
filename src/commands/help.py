from aiogram import Router, types
from aiogram.filters import Command

from src.handlers.help.help_handler import HelpCommandHandler
from src.utils.checking_permissions import checking_permissions

router = Router()


@router.message(Command("help"))
@checking_permissions
async def send_help(message: types.Message):
    handler = HelpCommandHandler()
    await handler.handle(message=message)
