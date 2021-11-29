from typing import List, Optional
import datetime

from pydantic import BaseModel


class UrlBase(BaseModel):
    ourl: str
    surl: str


class UrlCreate(UrlBase):
    ourl: str
    surl: str


class Url(UrlBase):
    id: int
    stamp: datetime.date

    class Config:
        orm_mode = True
