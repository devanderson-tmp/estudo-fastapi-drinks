from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
import secrets


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str
    DB_BASE_MODEL = declarative_base()

    ALGORITHM: str = "HS256"
    JWT_SECRET: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True
        env_file = ".env"


settings: Settings = Settings()
