from aiogram import Router, types
from aiogram.filters import Command

from src.constants.messages import TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST
from src.utils.checking_permissions import checking_permissions

router = Router()


@router.message(Command("add_visits"))
@checking_permissions
async def add_visits(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST,
        reply_markup=types.ForceReply(selective=True),
    )
