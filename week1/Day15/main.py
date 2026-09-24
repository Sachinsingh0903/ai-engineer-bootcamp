from fastapi import FastAPI

from config import settings

app = FastAPI(
    title=settings.app_name
)


@app.get("/")
def home():
    return {
        "application": settings.app_name,
        "environment": settings.environment,
        "debug": settings.debug
    }

@app.get("/config")
def config():
    return {
        "application": settings.app_name,
        "environment": settings.environment,
        "debug": settings.debug
    }