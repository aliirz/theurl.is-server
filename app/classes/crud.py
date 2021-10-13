from sqlalchemy.orm import Session

from . import models, schemas


def get_url(db: Session, surl: str):
    return db.query(models.Url).filter(models.Url.surl == surl).first()


def create_the_url(db: Session, url: schemas.UrlCreate):
    the_url = models.Url(
        ourl=url.ourl, surl=url.surl)
    db.add(the_url)
    db.commit()
    db.refresh(the_url)
    return the_url
