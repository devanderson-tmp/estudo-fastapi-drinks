from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_current_user, get_session
from models.drink_model import DrinkModel
from models.user_model import UserModel
from schemas.drink_schema import DrinkCreateSchema, DrinkSchema

router = APIRouter()


@router.post("/create", response_model=DrinkSchema, status_code=status.HTTP_201_CREATED)
async def create(
    drink: DrinkCreateSchema,
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    ingredients: str = ", ".join(drink.ingredients)
    new_drink = DrinkModel(
        name=drink.name,
        ingredients=ingredients,
        instructions=drink.instructions,
        user_id=current_user.id,
    )
    db.add(new_drink)
    await db.commit()
    return new_drink
