from fastapi import APIRouter

from api.v1.endpoints import drink, login, user

api = APIRouter()

api.include_router(login.router, tags=["Login"])
api.include_router(user.router, prefix="/users", tags=["Usuários"])
api.include_router(drink.router, prefix="/drinks", tags=["Drinks"])
