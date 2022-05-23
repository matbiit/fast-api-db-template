from db_conn import schemas
from db_conn.database import CloudantConnection
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from typing import List, Union

load_dotenv()


database = CloudantConnection()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search")
async def search(q: Union[str, None] = None):
    return {"q": q}

@app.get("/items", response_model=List[schemas.ItemResponse])
async def retrieve_items():
    db_services = database.retrieve_items()
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while retrieving items data")
    return db_services

@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
async def retrieve_item(item_id):
    db_services = database.retrieve_item(item_id)
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while retrieving item data")
    return db_services

@app.post("/items/")
async def create_item(item: schemas.Item):
    db_services = database.add_item(item)
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while inserting item data")
    return db_services

@app.put("/items/")
async def update_item(item: schemas.Item):
    db_services = database.update_item(item)
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while updating item data")
    return db_services

@app.delete("/items/")
async def delete_item(item: schemas.ItemDelete):
    db_services = database.delete_item(item)
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while deleting item data")
    return db_services
