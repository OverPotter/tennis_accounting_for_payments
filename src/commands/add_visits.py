from aiogram import Router, types
from aiogram.filters import Command

from src.constants.messages import TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST
from src.decorators.checking_permissions import checking_permissions
from src.schemas.enums.admin_roles import AdminRoleEnum

router = Router()


@router.message(Command("add_visits"))
@checking_permissions([AdminRoleEnum.ADMIN])
async def add_visits(message: types.Message):
    await message.answer(
        TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST,
        reply_markup=types.ForceReply(selective=True),
    )
