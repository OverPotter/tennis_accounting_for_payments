from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.database.models.models import ClientModel
from src.database.repositories.absctract_repository import AbstractRepository


class ClientRepository(AbstractRepository[ClientModel]):
    _model = ClientModel

    async def get_user_with_training_remains(self, client_name: str):
        query = (
            select(ClientModel)
            .options(joinedload(ClientModel.number_of_trainings_available))
            .filter_by(name=client_name)
        )

        result = await self._session.execute(query)

        client = result.scalars().first()
        return client
