from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.deps import get_session
from core.security import create_password_hash
from models.user_model import UserModel
from schemas.user_schema import UserSchema, UserCreateSchema

router = APIRouter()


@router.post("/create", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create(
    user: UserCreateSchema, db: AsyncSession = Depends(get_session)
) -> UserModel:
    async with db as session:
        query = select(UserModel).filter(UserModel.email == user.email)
        result = await session.execute(query)
        has_user = result.scalar_one_or_none()

        if has_user:
            raise HTTPException(
                detail="E-mail já cadastrado", status_code=status.HTTP_400_BAD_REQUEST
            )

    new_user = UserModel(
        name=user.name, email=user.email, password=create_password_hash(user.password)
    )
    db.add(new_user)
    await db.commit()
    return new_user
