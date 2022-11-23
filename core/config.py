import os
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_BASE_MODEL = declarative_base()
    SGBD: str
    USER: str
    PASSWORD: str
    SERVER: str
    DATABASE: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings: Settings = Settings()
