from typing import TypeVar

from sqlalchemy import Executable

from src.database.models.base import Base

MODEL_TYPE = TypeVar("MODEL_TYPE", bound=Base)
QUERY = TypeVar("QUERY", bound=Executable)
