from aiogram import types

from src.exceptions.entity_exceptions import EntityAlreadyExistException
from src.handlers.base import BaseCommandHandler
from src.services.collect_clients_data_service.abc import (
    AbstractCollectClientsDataService,
)
from src.services.create_empty_xlsx_service.abc import (
    AbstractCreateEmptyTableService,
)
from src.services.fill_in_xlsx_service.abc import AbstractFillInXlsxService


class CreateReportCommandHandler(BaseCommandHandler):
    def __init__(
        self,
        create_empty_xlsx_service: AbstractCreateEmptyTableService,
        collect_clients_data_service: AbstractCollectClientsDataService,
        fill_in_xlsx_service: AbstractFillInXlsxService,
    ):
        super().__init__()
        self._collect_clients_data_service = collect_clients_data_service
        self._create_empty_xlsx_service = create_empty_xlsx_service
        self._fill_in_xlsx_service = fill_in_xlsx_service

    async def handle(self, message: types.Message) -> None:
        # todo: create decorator to process all exceptions types
        try:
            report_name = self._create_empty_xlsx_service.create_xlsx_table()
            self._logger.debug(
                f"An empty file for the report has been created: {report_name}."
            )

            clients_data = (
                await self._collect_clients_data_service.collect_clients_data()
            )
            self._logger.debug("Customer data has been collected.")

            self._fill_in_xlsx_service.fill_in_xlsx(
                clients=clients_data, filename=report_name
            )
            self._logger.info(
                f"The report was created successfully: {report_name}."
            )

        except ValueError as e:
            self._logger.error(f"Validation failed: {str(e)}")
            await message.answer(f"Данные не валидны: {e}")

        except EntityAlreadyExistException as e:
            self._logger.error(f"User already exist: {e.details}")
            await message.answer("Такой пользователь уже существует.")
