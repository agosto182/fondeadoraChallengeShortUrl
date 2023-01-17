from fastapi import APIRouter, Depends
from services import urls
from models.url import UrlInput
from database import get_db

router = APIRouter()

@router.get("/")
async def get_index(db=Depends(get_db)):
    """GET index route"""
    response = {
            "message": "Hello world",
            "todo": "Please go to /docs to see the documentation"
    }
    return response

@router.get("/{code}")
async def get_url(code: str, db=Depends(get_db)):
    """GET route to get the original url from a code"""
    url = urls.get(db, code)
    return {"url": url.original_url}

@router.post("/")
async def create_url(body: UrlInput, db=Depends(get_db)):
    """POST route to create a new short url"""
    short_url = urls.create(db, body.url)
    return {"short_url": short_url}
