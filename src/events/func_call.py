from inspect import iscoroutinefunction
from typing import Callable, Coroutine, Generic, TypeVar

from src.events.abc import AbstractObserver, AbstractSubject

_T = TypeVar("_T")
WrappedFunctionType = Callable[
    [AbstractSubject[_T]], Coroutine[None, None, None] | None
]


class FuncCallObserver(AbstractObserver[_T], Generic[_T]):
    def __init__(
        self,
        function: WrappedFunctionType[_T],
    ) -> None:
        self._function = function

    async def handle_event(self, subject: AbstractSubject) -> None:
        if iscoroutinefunction(self._function):
            await self._function(subject)
        else:
            self._function(subject)
