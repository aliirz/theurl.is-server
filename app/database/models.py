from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime

from .database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    ourl = Column(String, unique=True, index=True)
    surl = Column(String)
    stamp = Column(Date, default=func.now())
