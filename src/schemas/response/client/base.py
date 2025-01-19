from src.schemas.response.base import BaseResponse


class ClientBaseResponse(BaseResponse):
    id: int
    name: str
