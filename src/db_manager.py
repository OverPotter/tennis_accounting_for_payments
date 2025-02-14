from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)

from src.decorators.singleton import singleton
from src.settings import settings_factory

settings = settings_factory()


@singleton
def engine_factory() -> AsyncEngine:
    return create_async_engine(
        settings.get_engine_link(),
        connect_args={},
    )


def session_factory() -> AsyncSession:
    engine = engine_factory()
    return AsyncSession(
        bind=engine,
        expire_on_commit=False,
        autoflush=False,
    )
