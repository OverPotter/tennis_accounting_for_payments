from src.services.fill_in_xlsx_service.abc import AbstractFillInXlsxService


class FacadeFillInXlsxService(AbstractFillInXlsxService):
    def __init__(self): ...

    def fill_in_xlsx(self) -> None: ...
