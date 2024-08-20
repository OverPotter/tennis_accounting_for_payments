from contextlib import asynccontextmanager
from typing import AsyncGenerator

from src.events.abc import AbstractSubject
from src.events.base import BaseSubject
from src.events.utils import observer


@asynccontextmanager
async def payments_creation_subject_context() -> (
    AsyncGenerator[AbstractSubject[BaseLegalEntityResponse], None]
):
    legal_entity_creation_subject: AbstractSubject[BaseLegalEntityResponse] = (
        BaseSubject()
    )

    @observer(legal_entity_creation_subject)
    def _(subject: AbstractSubject[BaseLegalEntityResponse]):
        if subject.state is not None:
            ...

    yield legal_entity_creation_subject
    await legal_entity_creation_subject.notify()
