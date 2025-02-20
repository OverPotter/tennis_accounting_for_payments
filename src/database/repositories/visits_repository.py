from datetime import datetime
from typing import Optional, Sequence

from sqlalchemy import desc
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from src.database.models.models import VisitModel
from src.database.repositories.absctract_repository import AbstractRepository


class VisitsRepository(AbstractRepository[VisitModel]):
    _model = VisitModel

    async def _fetch_client_history(
        self,
        client_id: int,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        coach_name: Optional[str] = None,
        strict_end: bool = True,
    ) -> Sequence[VisitModel]:
        query = (
            select(self._model)
            .options(joinedload(self._model.coach))
            .filter(self._model.client_id == client_id)
        )

        if start_date:
            query = query.filter(self._model.visit_datetime >= start_date)
        if end_date:
            query = query.filter(
                self._model.visit_datetime < end_date
                if strict_end
                else self._model.visit_datetime <= end_date
            )

        if coach_name:
            query = query.filter(self._model.coach.has(name=coach_name))

        query = query.order_by(desc(self._model.visit_datetime))

        result = await self._session.execute(query)
        return result.scalars().fetchall()

    async def get_all_client_visits_up_to_current_month(
        self,
        client_id: int,
        until_what_month: datetime.date,
        coach_name: str | None = None,
    ) -> Sequence[VisitModel]:
        return await self._fetch_client_history(
            client_id=client_id,
            end_date=until_what_month,
            coach_name=coach_name,
            strict_end=True,
        )

    async def get_monthly_client_visits(
        self,
        client_id: int,
        first_day_of_current_month: datetime.date,
        last_day_of_current_month: datetime.date,
        coach_name: str | None = None,
    ) -> Sequence[VisitModel]:
        return await self._fetch_client_history(
            client_id=client_id,
            start_date=first_day_of_current_month,
            end_date=last_day_of_current_month,
            coach_name=coach_name,
            strict_end=False,
        )
