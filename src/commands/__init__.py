from src.commands.add_client import router as add_client_router
from src.commands.add_payments import router as add_payments_router
from src.commands.help import router as help_router
from src.commands.processing_user_response import (
    router as processing_user_response_router,
)
from src.dispatcher.dispatcher import dp

dp.include_router(help_router)
dp.include_router(add_client_router)
dp.include_router(add_payments_router)
dp.include_router(processing_user_response_router)
