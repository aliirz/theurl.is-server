from fastapi import FastAPI
from classes.shortner import Shortener

app = FastAPI()


@app.get("/")
def read_root():
    return Shortener().generate_short_url()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
