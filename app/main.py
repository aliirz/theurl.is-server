import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session


from database import models, database, crud, schemas
from classes.shortner import Shortener
from classes.redirector import Redirector

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/", response_model=schemas.Url)
def make_the_url(url: schemas.UrlCreate, db: Session = Depends(get_db)):

    url.surl = Shortener().generate_the_url()
    the_url = crud.create_url(db, url)
    return the_url


@app.get("/{surl}", response_model=schemas.Url)
def get_the_url(surl: str, db: Session = Depends(get_db)):

    the_url = crud.get_url(db, surl)
    return Redirector().redirect(the_url.ourl)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1337)
