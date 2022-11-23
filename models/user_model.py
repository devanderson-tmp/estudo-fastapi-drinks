from sqlalchemy import Column, Integer, String

from core.config import settings


class UserModel(settings.DB_BASE_MODEL):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    email = Column(String(60), key="email", nullable=False, unique=True)
    password = Column(String(62), nullable=False)
