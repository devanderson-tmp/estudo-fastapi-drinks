from fastapi import APIRouter

from api.v1.endpoints import login, user

api = APIRouter()

api.include_router(login.router, tags=["Login"])
api.include_router(user.router, prefix="/users", tags=["Usuários"])
