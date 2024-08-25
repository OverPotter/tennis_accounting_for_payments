from datetime import datetime, timedelta

from sqlalchemy import func, select
from sqlalchemy.orm import joinedload

from src.database.models.models import ClientModel, VisitModel
from src.database.repositories.absctract_repository import AbstractRepository


class ClientRepository(AbstractRepository[ClientModel]):
    _model = ClientModel

    async def get_user_with_number_of_tennis_training_available(
        self, client_name: str
    ) -> _model | None:
        query = (
            select(ClientModel)
            .options(joinedload(ClientModel.number_of_trainings_available))
            .filter_by(name=client_name)
        )

        result = await self._session.execute(query)
        return result.unique().scalar_one_or_none()

    async def get_user_monthly_visits(self, client_name: str) -> _model | None:
        three_months_ago = datetime.now() - timedelta(days=90)

        query = (
            select(ClientModel)
            .options(joinedload(ClientModel.visits))
            .where(ClientModel.name == client_name)
            .join(VisitModel)
            .where(func.date(VisitModel.visit_datetime) >= three_months_ago)
            .order_by(VisitModel.visit_datetime.desc())
        )

        result = await self._session.execute(query)
        return result.unique().scalar_one_or_none()
