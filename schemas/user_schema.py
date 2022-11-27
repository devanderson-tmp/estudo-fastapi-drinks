from pydantic import BaseModel, EmailStr, validator
from typing import Optional


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr


class UserCreateSchema(UserBaseSchema):
    password: str

    @validator("name")
    def check_names_empty(cls, v):
        if v == "":
            raise ValueError("Nome é obrigatório")
        return v

    @validator("password")
    def check_password_empty(cls, v):
        if v == "":
            raise ValueError("Senha é obrigatório")
        return v


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
