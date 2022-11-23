from fastapi import FastAPI

from api.v1.api import api
from core.config import settings

app = FastAPI(title="Drinks")
app.include_router(api, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", log_level="info", port=8000, reload=True)
