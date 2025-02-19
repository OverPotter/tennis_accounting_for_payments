from datetime import datetime
from typing import Sequence

from src.database.models.models import VisitModel
from src.database.repositories.absctract_repository import AbstractRepository


class VisitsRepository(AbstractRepository[VisitModel]):
    _model = VisitModel

    async def get_all_client_visits_up_to_current_month(
        self,
        client_id: int,
        until_what_month: datetime.date,
        coach_name: str | None = None,
    ) -> Sequence[VisitModel]:
        return await self.get_all_by_client_up_to_date(
            client_id=client_id,
            date_field=VisitModel.visit_datetime.key,
            until_what_month=until_what_month,
            coach_name=coach_name,
        )

    async def get_monthly_client_visits(
        self,
        client_id: int,
        first_day_of_current_month: datetime.date,
        last_day_of_current_month: datetime.date,
        coach_name: str | None = None,
    ) -> Sequence[VisitModel]:
        return await self.get_monthly_client_entries(
            client_id=client_id,
            date_field=VisitModel.visit_datetime.key,
            first_day_of_current_month=first_day_of_current_month,
            last_day_of_current_month=last_day_of_current_month,
            coach_name=coach_name,
        )
