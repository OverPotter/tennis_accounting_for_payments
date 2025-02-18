from aiogram import Router, types
from aiogram.filters import Command

from src.constants.messages import HELP_TEXT
from src.decorators.checking_permissions import checking_permissions
from src.schemas.enums.admin_roles import AdminRoleEnum

router = Router()


@router.message(Command("help"))
@checking_permissions([AdminRoleEnum.ADMIN])
async def send_help(message: types.Message):
    await message.answer(HELP_TEXT)
