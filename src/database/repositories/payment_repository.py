from datetime import datetime
from typing import Optional, Sequence

from sqlalchemy import desc, select
from sqlalchemy.orm import joinedload

from src.database.models.models import PaymentModel
from src.database.repositories.absctract_repository import AbstractRepository


class PaymentRepository(AbstractRepository[PaymentModel]):
    _model = PaymentModel

    async def _fetch_client_history(
        self,
        client_id: int,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        coach_name: Optional[str] = None,
        strict_end: bool = True,
    ) -> Sequence[PaymentModel]:
        query = (
            select(self._model)
            .options(joinedload(self._model.coach))
            .filter(self._model.client_id == client_id)
        )

        if start_date:
            query = query.filter(self._model.payment_date >= start_date)
        if end_date:
            query = query.filter(
                self._model.payment_date < end_date
                if strict_end
                else self._model.payment_date <= end_date
            )

        if coach_name:
            query = query.filter(self._model.coach.has(name=coach_name))

        query = query.order_by(desc(self._model.payment_date))

        result = await self._session.execute(query)
        return result.scalars().fetchall()

    async def get_all_paid_client_training_up_to_current_month(
        self,
        client_id: int,
        until_what_month: datetime.date,
        coach_name: str | None = None,
    ) -> Sequence[PaymentModel]:
        return await self._fetch_client_history(
            client_id=client_id,
            end_date=until_what_month,
            coach_name=coach_name,
            strict_end=True,
        )

    async def get_monthly_client_paid_training_visits(
        self,
        client_id: int,
        first_day_of_current_month: datetime.date,
        last_day_of_current_month: datetime.date,
        coach_name: str | None = None,
    ) -> Sequence[PaymentModel]:
        return await self._fetch_client_history(
            client_id=client_id,
            start_date=first_day_of_current_month,
            end_date=last_day_of_current_month,
            coach_name=coach_name,
            strict_end=False,
        )
