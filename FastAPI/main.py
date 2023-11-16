from fastapi import FastAPI
from typing import Union # typing : List, Dick, Set, Final
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): # default the value of 'q' to 'None'
    return {"item_id" : item_id, "q":q}

#asd = read_item(2, "something")

"""
class Item(BaseModel):
    name:str
    price:float

#upgrades
@app.put('/items/{item_id}')
def update_item(item_id:int, item:Item):
    return {"item_id" : item_id, "item":item}

"""

"""
<Theory>
my_str:str
my_str_list: List 
my_str_list: List[st] = ["str1", "str2"]
Dict[str, int] = {
    'k':'v',
    'k':'v'
     }
    ==> 'k' : str
    =>  'v' : None, str, int (can be)
Dict [str, Union[None, str, int]]
"""
