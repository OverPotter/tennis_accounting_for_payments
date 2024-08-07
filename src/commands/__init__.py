import logging

from src.commands.start import router as start_router
from src.dispatcher.dispatcher import dp

logging.debug("Registering start_router")
dp.include_router(start_router)
