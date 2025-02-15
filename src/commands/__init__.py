from src.commands.add_client import router as add_client_router
from src.commands.add_coach import router as add_coach_router
from src.commands.add_payments import router as add_payments_router
from src.commands.add_visits import router as add_visits_router
from src.commands.create_report import router as create_report_router
from src.commands.get_monthly_payments import (
    router as get_monthly_payments_router,
)
from src.commands.get_monthly_visits import router as get_monthly_visits_router
from src.commands.get_number_of_tennis_training_available import (
    router as get_number_of_tennis_training_available_router,
)
from src.commands.help import router as help_router
from src.commands.processing_user_response import (
    router as processing_user_response_router,
)
from src.dispatcher.dispatcher import dp
from src.middleware.error_handler_middleware import ErrorHandlerMiddleware

dp.message.middleware(ErrorHandlerMiddleware())

dp.include_router(create_report_router)
dp.include_router(add_client_router)
dp.include_router(add_coach_router)
dp.include_router(add_payments_router)
dp.include_router(add_visits_router)
dp.include_router(get_monthly_payments_router)
dp.include_router(get_monthly_visits_router)
dp.include_router(get_number_of_tennis_training_available_router)
dp.include_router(help_router)
dp.include_router(processing_user_response_router)
