from abc import ABC
from typing import Generic, Sequence, Type

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

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
