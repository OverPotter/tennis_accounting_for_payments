from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class BaseIDModel(Base):
    __abstract__ = True
    __table_args__ = ()

    id = Column(Integer, primary_key=True, autoincrement=True)
