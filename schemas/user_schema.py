from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
