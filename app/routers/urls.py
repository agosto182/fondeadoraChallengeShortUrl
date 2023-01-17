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
    code = urls.create(db, body.url)

    # Here hardcoded but it needs to be depending of the stage env
    short_url = f'http://127.0.0.1:8000/{code}'
    return {"short_url": short_url}
