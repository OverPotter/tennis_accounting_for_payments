from src.database.models.models import ClientModel
from src.database.repositories.absctract_repository import AbstractRepository


class ClientRepository(AbstractRepository[ClientModel]):
    _model = ClientModel
