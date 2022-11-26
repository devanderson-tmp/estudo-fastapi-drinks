from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional

from core.auth import oauth2_schema
from core.config import settings
from core.database import Session
from models.user_model import UserModel
from schemas.user_schema import UserSchema


class TokenData(BaseModel):
    username: Optional[str] = None


async def get_session():
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()


async def get_current_user(
    db: Session = Depends(get_session), token: str = Depends(oauth2_schema)
) -> UserSchema:
    credential_exception = HTTPException(
        detail="Usuário não autorizado",
        headers="WWW-Authenticate: 'Bearer'",
        status_code=status.HTTP_401_UNAUTHORIZED,
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")

        if username is None:
            raise credential_exception

        token_data: TokenData = TokenData(username=username)
    except JWTError:
        raise credential_exception

    async with db as session:
        query = select(UserModel).filter(UserModel.email == token_data.username)
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()

        if user is None:
            raise credential_exception

        return user
