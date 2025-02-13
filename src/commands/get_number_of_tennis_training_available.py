from aiogram import Router, types
from aiogram.filters import Command

from src.constants.messages import (
    TEXT_OF_MESSAGE_FOR_GET_NUMBER_OF_TENNIS_TRAINING_AVAILABLE_REQUEST,
)
from src.decorators.checking_permissions import checking_permissions

router = Router()


@router.message(Command("get_number_of_tennis_training"))
@checking_permissions
async def get_number_of_tennis_training_available(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_GET_NUMBER_OF_TENNIS_TRAINING_AVAILABLE_REQUEST,
        reply_markup=types.ForceReply(selective=True),
    )
