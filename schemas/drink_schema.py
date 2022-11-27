from pydantic import BaseModel, validator
from typing import List, Optional


class DrinkBaseSchema(BaseModel):
    name: str
    ingredients: List[str]
    instructions: str


class DrinkCreateSchema(DrinkBaseSchema):
    @validator("name")
    def check_names_empty(cls, v):
        if v == "":
            raise ValueError("Nome é obrigatório")
        return v

    @validator("instructions")
    def check_instructions_empty(cls, v):
        if v == "":
            raise ValueError("Instrução é obrigatório")
        return v

    @validator("ingredients")
    def check_ingredients_empty(cls, v):
        for ingredient in v:
            assert ingredient != "", "Ingrediente é obrigatório"
        return v


class DrinkSchema(BaseModel):
    id: Optional[int] = None
    name: str
    ingredients: str
    instructions: str
    user_id: Optional[int]

    class Config:
        orm_mode = True
