from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.config import settings


class DrinkModel(settings.DB_BASE_MODEL):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    ingredients = Column(String(255), nullable=False)
    instructions = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("UserModel", back_populates="drinks", lazy="joined")
