import datetime
from typing import Annotated

from sqlalchemy import String, func
from sqlalchemy.orm import mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]

created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=func.now(), onupdate=func.now()),
]

token = Annotated[str, mapped_column(String(255), nullable=False)]
