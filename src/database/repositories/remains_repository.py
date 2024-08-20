from src.database.models.models import NumberOfTennisTrainingAvailable
from src.database.repositories.absctract_repository import AbstractRepository


class RemainsRepository(AbstractRepository[NumberOfTennisTrainingAvailable]):
    _model = NumberOfTennisTrainingAvailable
