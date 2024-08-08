from sqlalchemy.orm import DeclarativeBase, Mapped

from src.database.models._universal_type_annotations import intpk


class Base(DeclarativeBase):
    pass


class BaseIDModel(Base):
    __abstract__ = True
    __table_args__ = ()

    id: Mapped[intpk]
