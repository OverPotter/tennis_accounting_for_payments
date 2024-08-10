from src.database.models.models import PaymentModel
from src.database.repositories.absctract_repository import AbstractRepository


class PaymentRepository(AbstractRepository[PaymentModel]):
    _model = PaymentModel
