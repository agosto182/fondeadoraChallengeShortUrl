from fastapi import APIRouter, Depends
from models.url import UrlInput
from database import get_db

router = APIRouter()

@router.get('/{code}')
async def getUrl(code: str, db = Depends(get_db)):
    return { 'url': 'asd', 'code': code }

@router.post('/')
async def createUrl(body: UrlInput, db = Depends(get_db)):
    return { 'url': body.url }
