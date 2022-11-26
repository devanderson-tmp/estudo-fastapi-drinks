from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from core.auth import authenticate, create_access_token
from core.deps import get_current_user, get_session
from models.user_model import UserModel
from schemas.user_schema import UserSchema

router = APIRouter()


@router.post("/login/access-token")
async def login(
    db: AsyncSession = Depends(get_session),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = await authenticate(
        db=db, email=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(
            detail="Usuário ou senha incorretos",
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return JSONResponse(
        content={
            "access_token": create_access_token(sub=user.email),
        },
        status_code=status.HTTP_200_OK,
    )


@router.post("/login/test-token", response_model=UserSchema)
async def test_token(current_user: UserModel = Depends(get_current_user)):
    return current_user
