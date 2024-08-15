from src.commands.add_client import router as add_client_router
from src.commands.add_payments import router as add_payment_router
from src.commands.add_visits import router as add_visits_router
from src.commands.help import router as help_router
from src.dispatcher.dispatcher import dp

dp.include_router(help_router)
dp.include_router(add_client_router)
dp.include_router(add_payment_router)
dp.include_router(add_visits_router)
