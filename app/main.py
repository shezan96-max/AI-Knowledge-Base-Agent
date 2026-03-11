from fastapi import FastAPI
from app.api.routers.ask import router as ask_router
from app.api.routers.upload import router as upload_router
from app.api.routers.analytics import router as analytics_router


app = FastAPI()


app.include_router(ask_router)
app.include_router(upload_router)
app.include_router(analytics_router)