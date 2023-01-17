import logging
import random
import string
from fastapi import HTTPException 
from sqlalchemy.orm import Session
from models.url import Url

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.DEBUG)

def create(db: Session, url: str):
    logger.info("Trying to create new url with: %s", url)
    try:
        random_code = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        logger.info("New code is %s", random_code)
        url = Url(original_url=url, short_url=random_code)
        logger.info("New url object created %s", url.__dict__)
        db.add(url)
        db.commit()
        return url.short_url
    except Exception as exception:
        logger.exception(exception)
        raise HTTPException(status_code=500, detail="An error as ocurred")

def get(db: Session, code: str):
    logger.info("Looking for url with code %s", code)
    try:
        url = db.query(Url).filter_by(short_url=code).one()
        logger.info("Url found %s", url)
        return url
    except Exception:
        logger.error("url not found")
        raise HTTPException(status_code=404, detail="Not found")
