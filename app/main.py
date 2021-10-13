import uvicorn
from fastapi import FastAPI
from classes.shortner import Shortener


from database import models, database, crud, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.get("/")
def read_root():
    return Shortener().generate_the_url()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
