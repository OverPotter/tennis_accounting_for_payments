from contextlib import asynccontextmanager
from typing import AsyncGenerator

from src.events.abc import AbstractSubject
from src.events.base import BaseSubject
from src.events.utils import observer
from src.schemas.response.payment.base import PaymentBaseResponse


@asynccontextmanager
async def payment_creation_subject_context() -> (
    AsyncGenerator[AbstractSubject[PaymentBaseResponse], None]
):
    payment_creation_subject: AbstractSubject[PaymentBaseResponse] = (
        BaseSubject()
    )

    @observer(payment_creation_subject)
    def _(subject: AbstractSubject[PaymentBaseResponse]):
        if subject.state is not None:
            ...

    yield payment_creation_subject
    await payment_creation_subject.notify()
