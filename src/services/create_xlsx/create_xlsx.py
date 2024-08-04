import locale

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

from src.constants import TMP_DIR
from src.services.create_xlsx.abc import AbstractCreateTableService
from src.utils.get_number_of_days_in_month import get_number_of_days_in_month


class CreateExcelTableService(AbstractCreateTableService):
    @staticmethod
    async def create_xlsx_table():
        number_days_of_in_month, current_month_name, current_year = (
            get_number_of_days_in_month()
        )

        locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

        wb = Workbook()
        ws = wb.active

        sub_headers_month = [
            "ФИО",
            "Остаточный переход",
            "Количество",
            "Сумма оплаты",
            "Количество тренировок",
            "Дата оплаты",
        ]

        ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=6)
        ws.merge_cells(
            start_row=1,
            start_column=7,
            end_row=1,
            end_column=6 + number_days_of_in_month,
        )
        ws.merge_cells(
            start_row=1,
            start_column=6 + number_days_of_in_month + 1,
            end_row=1,
            end_column=6 + number_days_of_in_month + 1,
        )

        dark_green_fill = PatternFill(
            start_color="006400", end_color="006400", fill_type="solid"
        )
        black_font = Font(color="000000")

        ws.cell(row=1, column=1, value=current_month_name.capitalize()).alignment = (
            Alignment(horizontal="center", vertical="center")
        )
        ws.cell(row=1, column=1).fill = dark_green_fill
        ws.cell(row=1, column=1).font = black_font

        ws.cell(row=1, column=7, value="Дата").alignment = Alignment(
            horizontal="center", vertical="center"
        )
        ws.cell(row=1, column=7).fill = dark_green_fill
        ws.cell(row=1, column=7).font = black_font

        ws.cell(
            row=1,
            column=6 + number_days_of_in_month + 1,
            value="Количество оставшихся тренировок",
        ).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=1, column=6 + number_days_of_in_month + 1).fill = dark_green_fill
        ws.cell(row=1, column=6 + number_days_of_in_month + 1).font = black_font

        for col in range(1, 7 + number_days_of_in_month + 1):
            cell = ws.cell(row=1, column=col)
            cell.fill = dark_green_fill
            cell.font = black_font

        for i, sub_header in enumerate(sub_headers_month):
            cell = ws.cell(row=2, column=i + 1, value=sub_header)
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.fill = dark_green_fill
            cell.font = black_font

        for day in range(1, number_days_of_in_month + 1):
            cell = ws.cell(row=2, column=6 + day, value=day)
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.fill = dark_green_fill
            cell.font = black_font

        filename = f"{TMP_DIR}/{current_month_name}_{current_year}.xlsx"
        wb.save(filename)
