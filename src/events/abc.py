from abc import ABC, abstractmethod
from typing import Generic, TypeVar

_T = TypeVar("_T")


class AbstractSubject(ABC, Generic[_T]):
    def __init__(self) -> None:
        self.state: _T | None = None

    @abstractmethod
    def attach(self, observer: "AbstractObserver") -> None:
        """attach observer to subject"""

    @abstractmethod
    def detach(self, observer: "AbstractObserver") -> None:
        """detach observer from subject"""

    @abstractmethod
    async def notify(self) -> None:
        """notify all observers about event"""

    @abstractmethod
    async def update(self, state: _T) -> None:
        """update state"""


class AbstractObserver(ABC, Generic[_T]):
    @abstractmethod
    async def handle_event(self, subject: AbstractSubject[_T]) -> None: ...
