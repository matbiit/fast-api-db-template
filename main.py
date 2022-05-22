from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search")
async def search(q: Union[str, None] = None):
    return {"q": q}