from abc import ABC, abstractmethod


class AbstractFillInXlsxService(ABC):
    @abstractmethod
    def fill_in_xlsx(self) -> None: ...
