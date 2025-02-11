from abc import ABC, abstractmethod

from aiogram import types


class AbstractSendReportService(ABC):
    @abstractmethod
    async def send_report(
        self, message: types.Message, report_path: str
    ) -> None: ...
