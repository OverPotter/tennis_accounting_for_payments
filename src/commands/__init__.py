from src.commands.help import router as help_router
from src.dispatcher.dispatcher import dp

dp.include_router(help_router)
