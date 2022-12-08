from pydantic import BaseModel, validator
from typing import List, Optional


class DrinkBaseSchema(BaseModel):
    name: str
    ingredients: List[str]
    instruction: str


class DrinkCreateSchema(DrinkBaseSchema):
    @validator("name")
    def check_name_is_empty(cls, v):
        if v == "":
            raise ValueError("Nome é obrigatório")
        return v

    @validator("instruction")
    def check_instruction_is_empty(cls, v):
        if v == "":
            raise ValueError("Instrução é obrigatório")
        return v

    @validator("ingredients")
    def check_ingredients_list_is_empty(cls, v):
        for ingredient in v:
            assert ingredient != "", "Ingrediente é obrigatório"
        return v


class DrinkSchema(BaseModel):
    id: Optional[int] = None
    name: str
    ingredients: str
    instruction: str
    user_id: Optional[int]

    class Config:
        orm_mode = True
