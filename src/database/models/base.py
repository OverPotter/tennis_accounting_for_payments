from sqlalchemy.orm import DeclarativeBase, Mapped

from src.database.models._universal_type_annotations import created_at, updated_at


class Base(DeclarativeBase): ...


class CreatedUpdatedModel(Base):
    __abstract__ = True

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
