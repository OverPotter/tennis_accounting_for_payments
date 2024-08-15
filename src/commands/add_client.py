from aiogram import Router, types
from aiogram.filters import Command

from src.constants_text import TEXT_OF_MESSAGE_FOR_ADD_CLIENT_REQUEST
from src.utils.checking_permissions import checking_permissions

router = Router()


@router.message(Command("add_client"))
@checking_permissions
async def add_client(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_ADD_CLIENT_REQUEST,
        reply_markup=types.ForceReply(selective=True),
    )
