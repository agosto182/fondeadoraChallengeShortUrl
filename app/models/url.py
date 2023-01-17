from sqlalchemy import Column, ForeignKey, Integer, String
from pydantic import BaseModel

from database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String)
    short_url = Column(String, unique=True)


class UrlInput(BaseModel):
    url: str
