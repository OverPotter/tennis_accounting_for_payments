from aiogram import Router, types
from aiogram.filters import Command

from src.constants.messages import HELP_TEXT
from src.utils.checking_permissions import checking_permissions

router = Router()


@router.message(Command("help"))
@checking_permissions
async def send_help(message: types.Message):
    await message.answer(HELP_TEXT)
