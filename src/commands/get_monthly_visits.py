from aiogram import Router, types
from aiogram.filters import Command

from src.constants_text import TEXT_OF_MESSAGE_FOR_GET_MONTHLY_VISITS_REQUEST
from src.utils.checking_permissions import checking_permissions

router = Router()


@router.message(Command("get_monthly_visits"))
@checking_permissions
async def get_monthly_visits(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_GET_MONTHLY_VISITS_REQUEST,
        reply_markup=types.ForceReply(selective=True),
    )
