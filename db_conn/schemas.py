from pickletools import int4
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    desc: str
    amount: int

class ItemResponse(BaseModel):
    _id: str
    _rev: str
    desc: str
    amount: int

class ItemDelete(BaseModel):
    id: int
