from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import EmailStr
from pytz import timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional

from core.config import settings
from core.security import password_verify
from models.user_model import UserModel

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


async def authenticate(
    email: EmailStr, password: str, db: AsyncSession
) -> Optional[UserModel]:
    async with db as session:
        query = select(UserModel).filter(UserModel.email == email)
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()

        if not user:
            return None

        if not password_verify(password, user.password):
            return None

        return user


def _create_token(token_type: str, timelife: timedelta, sub: str) -> str:
    payload = {}
    sp = timezone("America/Sao_Paulo")
    expire = datetime.now(tz=sp) + timelife

    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, settings.ALGORITHM)


def create_access_token(sub: str) -> str:
    return _create_token(
        token_type="access_token",
        timelife=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
    )
