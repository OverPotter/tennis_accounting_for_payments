from aiogram import Router, types
from aiogram.filters import Command

from src.constants_text import TEXT_OF_MESSAGE_FOR_GET_REMAINS_REQUEST
from src.utils.checking_permissions import checking_permissions

router = Router()


@router.message(Command("get_remains"))
@checking_permissions
async def get_remains(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_GET_REMAINS_REQUEST,
        reply_markup=types.ForceReply(selective=True),
    )
