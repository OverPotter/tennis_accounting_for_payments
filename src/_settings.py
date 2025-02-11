from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.constants.paths import ENV_PATH

load_dotenv()


class Settings(BaseSettings):
    PG_HOST: str
    PG_USER: str
    PG_PASS: str
    PG_PORT: str
    PG_DB_NAME: str

    DB_DRIVER: str

    REQUEST_TIMEOUT: int = 60
    DEBUG: bool = False

    API_TOKEN: str

    def get_engine_link(self) -> str:
        return f"{self.DB_DRIVER}://{self.PG_USER}:{self.PG_PASS}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB_NAME}"

    model_config = SettingsConfigDict(extra="ignore")


def settings_factory() -> Settings:
    return Settings(_env_file=ENV_PATH)
