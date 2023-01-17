from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models.url import Url
from database import SessionLocal, engine, Base
from routers import urls

import logging

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(urls.router)

@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn")
    logger.info("Log started")
