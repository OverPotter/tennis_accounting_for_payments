from src.database.models.models import VisitModel
from src.database.repositories.absctract_repository import AbstractRepository


class MonthlyVisitsRepository(AbstractRepository[VisitModel]):
    _model = VisitModel
