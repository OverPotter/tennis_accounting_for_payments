from datetime import datetime
from typing import Sequence

from sqlalchemy import desc, select

from src.database.models.models import VisitModel
from src.database.repositories.absctract_repository import AbstractRepository


class VisitsRepository(AbstractRepository[VisitModel]):
    _model = VisitModel

    async def get_all_client_visits_up_to_current_month(
        self, client_id: int, until_what_month: datetime.date
    ) -> Sequence[VisitModel]:
        query = (
            select(VisitModel)
            .filter(
                VisitModel.client_id == client_id,
                VisitModel.visit_datetime < until_what_month,
            )
            .order_by(desc(VisitModel.visit_datetime))
        )

        result = await self._session.execute(query)
        return result.scalars().fetchall()

    async def get_monthly_client_visits(
        self,
        client_id: int,
        first_day_of_current_month: datetime.date,
        last_day_of_current_month: datetime.date,
    ) -> Sequence[VisitModel]:
        query = (
            select(VisitModel)
            .filter(
                VisitModel.client_id == client_id,
                VisitModel.visit_datetime >= first_day_of_current_month,
                VisitModel.visit_datetime <= last_day_of_current_month,
            )
            .order_by(desc(VisitModel.visit_datetime))
        )

        result = await self._session.execute(query)
        return result.scalars().fetchall()
