from aiogram import Router, types
from aiogram.filters import Command

from src.handlers.start.start_handler import StartCommandHandler

router = Router()


@router.message(Command("start"))
async def send_welcome(message: types.Message):
    handler = StartCommandHandler()
    await handler.handle(message=message)
