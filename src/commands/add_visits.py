from aiogram import Router, types
from aiogram.filters import Command

from src.constants_text import TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST

router = Router()


@router.message(Command("add_visits"))
async def add_visits(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST,
        reply_markup=types.ForceReply(selective=True),
    )
