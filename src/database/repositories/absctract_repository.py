from abc import ABC
from datetime import datetime
from typing import Generic, Optional, Sequence, Type

from sqlalchemy import delete, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from src.constants.custom_types import MODEL_TYPE


class AbstractRepository(ABC, Generic[MODEL_TYPE]):
    _model: Type[MODEL_TYPE] | None = None

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all(self) -> Sequence[MODEL_TYPE]:
        query = select(self._model)
        result = await self._session.execute(query)
        return result.scalars().all()

    async def create(self, **kwargs) -> MODEL_TYPE:
        entity = self._model(**kwargs)
        self._session.add(entity)
        await self._session.commit()
        return entity

    async def get(self, **kwargs) -> MODEL_TYPE:
        result = await self._session.execute(
            select(self._model).filter_by(**kwargs)
        )
        entity = result.scalars().first()
        return entity

    async def delete(self, **kwargs) -> None:
        query = delete(self._model).filter_by(**kwargs)
        await self._session.execute(query)

    async def _fetch_client_history(
        self,
        client_id: int,
        date_field: str,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
        coach_name: Optional[str] = None,
        strict_end: bool = True,
    ) -> Sequence[MODEL_TYPE]:
        query = (
            select(self._model)
            .options(joinedload(self._model.coach))
            .filter(getattr(self._model, "client_id") == client_id)
        )

        if start_date:
            query = query.filter(getattr(self._model, date_field) >= start_date)
        if end_date:
            if strict_end:
                query = query.filter(
                    getattr(self._model, date_field) < end_date
                )
            else:
                query = query.filter(
                    getattr(self._model, date_field) <= end_date
                )

        if coach_name:
            query = query.filter(self._model.coach.has(name=coach_name))

        query = query.order_by(desc(getattr(self._model, date_field)))

        result = await self._session.execute(query)
        return result.scalars().fetchall()

    async def get_all_by_client_up_to_date(
        self,
        client_id: int,
        date_field: str,
        until_what_month: datetime.date,
        coach_name: Optional[str] = None,
    ) -> Sequence[MODEL_TYPE]:
        return await self._fetch_client_history(
            client_id=client_id,
            date_field=date_field,
            end_date=until_what_month,
            coach_name=coach_name,
            strict_end=True,
        )

    async def get_monthly_client_entries(
        self,
        client_id: int,
        date_field: str,
        first_day_of_current_month: datetime.date,
        last_day_of_current_month: datetime.date,
        coach_name: Optional[str] = None,
    ) -> Sequence[MODEL_TYPE]:
        return await self._fetch_client_history(
            client_id=client_id,
            date_field=date_field,
            start_date=first_day_of_current_month,
            end_date=last_day_of_current_month,
            coach_name=coach_name,
            strict_end=False,
        )
