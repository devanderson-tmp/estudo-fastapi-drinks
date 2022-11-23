from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str
    DB_BASE_MODEL = declarative_base()

    class Config:
        case_sensitive = True
        env_file = ".env"


settings: Settings = Settings()
