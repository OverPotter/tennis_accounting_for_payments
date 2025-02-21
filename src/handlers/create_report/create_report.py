from aiogram import types

from src.decorators.error_handler import error_handler
from src.handlers.base import BaseCommandHandler
from src.services.collect_clients_data_service.abc import (
    AbstractCollectClientsDataService,
)
from src.services.create_empty_xlsx_service.abc import (
    AbstractCreateEmptyTableService,
)
from src.services.fill_in_xlsx_service.abc import AbstractFillInXlsxService
from src.services.send_report_service.abc import AbstractSendReportService
from src.utils.validators.validate_name import validate_full_name


class CreateReportCommandHandler(BaseCommandHandler):
    def __init__(
        self,
        create_empty_xlsx_service: AbstractCreateEmptyTableService,
        collect_clients_data_service: AbstractCollectClientsDataService,
        fill_in_xlsx_service: AbstractFillInXlsxService,
        send_report_service: AbstractSendReportService,
    ):
        super().__init__()
        self._collect_clients_data_service = collect_clients_data_service
        self._create_empty_xlsx_service = create_empty_xlsx_service
        self._fill_in_xlsx_service = fill_in_xlsx_service
        self._send_report_service = send_report_service

    @error_handler
    async def handle(self, message: types.Message) -> None:
        coach_name = validate_full_name(message.text)

        report_path = await self._create_empty_xlsx_service.create_xlsx_table()
        self._logger.debug(
            f"An empty file for the report has been created: {report_path}."
        )

        clients_data = (
            await self._collect_clients_data_service.collect_clients_data(
                coach_name=coach_name
            )
        )
        self._logger.debug("Customer data has been collected.")

        self._fill_in_xlsx_service.fill_in_xlsx(
            clients=clients_data, filename=report_path
        )
        self._logger.debug(
            f"The report was created successfully: {report_path}."
        )

        await self._send_report_service.send_report(
            message=message, report_path=report_path
        )
        self._logger.info("The report was sent successfully.")
