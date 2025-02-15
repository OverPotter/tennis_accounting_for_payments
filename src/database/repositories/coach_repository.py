from src.database.models.models import CoachModel
from src.database.repositories.absctract_repository import AbstractRepository


class CoachRepository(AbstractRepository[CoachModel]):
    _model = CoachModel
