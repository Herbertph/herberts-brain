from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.ask import router as ask_router

app = FastAPI(
    title="Herbert's Brain API",
    version="1.0.0",
    debug=True,
)

app.include_router(health_router)
app.include_router(ask_router)
