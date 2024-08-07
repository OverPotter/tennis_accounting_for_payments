from aiogram import types


class StartCommandHandler:

    async def handle(self, message: types.Message):
        # Отправка приветственного сообщения
        await message.answer("Привет! Добро пожаловать в наш бот по теннису!")
