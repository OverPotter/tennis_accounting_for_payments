from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    MD_USER: str
    MD_PASS: str
    MD_HOST: str
    MD_PORT: str
    MD_DB_NAME: str

    def get_engine_link(self) -> str:
        return f"mysql+aiomysql://{self.MD_USER}:{self.MD_PASS}@{self.MD_HOST}:{self.MD_PORT}/{self.MD_DB_NAME}"

    model_config = SettingsConfigDict(extra="ignore")


def settings_factory() -> Settings:
    return Settings(_env_file=".env")
