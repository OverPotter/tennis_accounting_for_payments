from src.database.models.models import NumberOfTennisTrainingAvailable
from src.database.repositories.absctract_repository import AbstractRepository


class NumberOfTennisTrainingAvailableRepository(
    AbstractRepository[NumberOfTennisTrainingAvailable]
):
    _model = NumberOfTennisTrainingAvailable
