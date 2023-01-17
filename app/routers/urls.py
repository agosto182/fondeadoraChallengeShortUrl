from fastapi import APIRouter, Depends
from services import urls
from models.url import UrlInput
from database import get_db

router = APIRouter()

@router.get('/')
async def get_index(db = Depends(get_db)):
    return { 'url': 'asd' }


@router.get('/{code}')
async def get_url(code: str, db = Depends(get_db)):
    url = urls.get(db, code)
    return { 'url': url.original_url }

@router.post('/')
async def create_url(body: UrlInput, db = Depends(get_db)):
    short_url = urls.create(db, body.url)
    return { 'short_url': short_url }
