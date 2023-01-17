from fastapi import FastAPI

from database import engine, Base
from routers import urls

import logging

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(urls.router)


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn")
    logger.info("Log started")
