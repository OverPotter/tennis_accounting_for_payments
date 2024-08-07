from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token="YOUR_BOT_TOKEN_HERE")
dp = Dispatcher(storage=MemoryStorage())
