from pydantic import BaseModel
from typing import Optional


class UserBaseSchema(BaseModel):
    name: str


class UserCreateSchema(UserBaseSchema):
    pass


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str

    class Config:
        orm_mode = True
