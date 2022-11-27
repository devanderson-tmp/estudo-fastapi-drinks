from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

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


@router.get("/{id}", response_model=DrinkSchema, status_code=status.HTTP_200_OK)
async def show(
    id: int,
    current_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session),
):
    async with db as session:
        query = select(DrinkModel).filter(
            DrinkModel.id == id, DrinkModel.user_id == current_user.id
        )
        result = await session.execute(query)
        drink: DrinkModel = result.scalars().unique().one_or_none()

        if not drink:
            raise HTTPException(
                detail="Drink não encontrado", status_code=status.HTTP_204_NO_CONTENT
            )

        return drink
