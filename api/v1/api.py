from fastapi import APIRouter

from api.v1.endpoints import user

api = APIRouter()

api.include_router(user.router, prefix="/users", tags=["Usuários"])
