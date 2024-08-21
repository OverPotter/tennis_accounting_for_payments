from typing import Generic, TypeVar

from src.events.abc import AbstractObserver, AbstractSubject

_T = TypeVar("_T")


class BaseSubject(AbstractSubject[_T], Generic[_T]):
    def __init__(self) -> None:
        self._observers: set[AbstractObserver] = set()
        super().__init__()

    def attach(self, observer: "AbstractObserver") -> None:
        self._observers.add(observer)

    def detach(self, observer: "AbstractObserver") -> None:
        self._observers.remove(observer)

    async def update(self, state: _T) -> None:
        self.state = state

    async def notify(self) -> None:
        for observer in self._observers:
            await observer.handle_event(self)
