from sqlalchemy import select

from src.database.models.models import AdminModel
from src.database.repositories.absctract_repository import AbstractRepository


class AdminRepository(AbstractRepository[AdminModel]):
    _model = AdminModel

    async def is_admin(self, tg_id: int) -> bool:
        query = select(AdminModel).filter_by(tg_id=tg_id)
        result = await self._session.execute(query)
        return bool(result.scalars().first())
