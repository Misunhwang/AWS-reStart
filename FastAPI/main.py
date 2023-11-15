from fastapi import FastAPI
from typing import Union # typing : List, Dick, Set, Final
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id" : item_id, "q":q}

class Item(BaseModel):
    name:str
    price:float

#upgrades
@app.put('/items/{item_id}')
def update_item(item_id:int, item:Item):
    return {"item_id" : item_id, "item":item}