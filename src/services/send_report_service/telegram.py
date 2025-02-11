from aiogram import types
from aiogram.types import FSInputFile

from src.services.send_report_service.abc import AbstractSendReportService


class TelegramSendReportService(AbstractSendReportService):
    async def send_report(
        self, message: types.Message, report_path: str
    ) -> None:
        file_to_send = FSInputFile(report_path)
        await message.answer_document(file_to_send)
