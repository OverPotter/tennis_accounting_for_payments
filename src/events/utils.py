from typing import TypeVar

from src.events.abc import AbstractObserver, AbstractSubject
from src.events.func_call import FuncCallObserver, WrappedFunctionType

_T = TypeVar("_T")
_V = TypeVar("_V", bound=WrappedFunctionType)


def observer(subject: AbstractSubject[_T]):
    def decorator(
        func: _V,
    ) -> _V:
        observer: AbstractObserver[_T] = FuncCallObserver(func)
        subject.attach(observer)
        return func

    return decorator
