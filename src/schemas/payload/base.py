from pydantic import BaseModel


class BasePayload(BaseModel):
    class Config:
        from_attributes = True
        alias_generator = "to_camel"
