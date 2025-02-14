from aiogram import Router, types
from aiogram.filters import Command

from src.constants.messages import TEXT_OF_MESSAGE_FOR_CREATE_REPORT
from src.decorators.checking_permissions import checking_permissions

router = Router()


@router.message(Command("create_report"))
@checking_permissions
async def create_report(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_CREATE_REPORT,
        reply_markup=types.ForceReply(selective=True),
    )
