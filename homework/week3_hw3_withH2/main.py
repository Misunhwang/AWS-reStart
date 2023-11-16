# 1) Start main.py
from dto import Author, BookStore, BookItem

from typing import Dict, List
from fastapi import FastAPI, HTTPException

app = FastAPI()

# 2) Define my_book_item_dict Dictionary
my_book_item_dict: Dict[str, BookItem] = {}

# 3) Create 'PUT' APIs
@app.put("/books/{name}")
def create_item(item: BookItem, name: str) -> None :
    my_book_item_dict[name] = item
    print(my_book_item_dict)

# 4) Create 'GET' APIs, Handle exception 404
@app.get("/books/{name}")
def get_item(name: str) -> BookItem :
    if name in my_book_item_dict.keys():
        return my_book_item_dict[name]
    else:
        raise HTTPException(status_code=404, detail="Item not found : " + name)
 
# 5) Create 'Delete' APIs
@app.delete("/books/{name}")
def delete_item(name: str) -> Dict :
    if name in my_book_item_dict.keys():
        my_book_item_dict.pop(name)
        print(my_book_item_dict)
        return {"msg":"Successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found : " + name)

# 6) Create 'GET' APIs (all items saved)   
@app.get("/books/")
def get_items() -> List[BookItem]:
    return my_book_item_dict.values()

