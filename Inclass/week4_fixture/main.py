# 1) Start main.py
from dto import InventoryItem, ItemOrigin

from typing import Dict, List
from fastapi import FastAPI, HTTPException

app = FastAPI()

# 2) Define my_inventory_item_dict Dictionary
my_inventory_item_dict: Dict[str, InventoryItem] = {}

# 3) Create 'PUT' APIs
@app.put("/items/{serial_num}")
def create_item(item: InventoryItem, serial_num: str) -> None :
    my_inventory_item_dict[serial_num] = item
    print(my_inventory_item_dict)

# 4) Create 'GET' APIs, Handle exception 404
@app.get("/items/{serial_num}")
def get_item(serial_num: str) -> InventoryItem :
    if serial_num in my_inventory_item_dict.keys():
        return my_inventory_item_dict[serial_num]
    else:
        raise HTTPException(status_code=404, detail="Item not found : " + serial_num)
 
# 5) Create 'Delete' APIs
@app.delete("/items/{serial_num}")
def delete_item(serial_num: str) -> Dict :
    if serial_num in my_inventory_item_dict.keys():
        my_inventory_item_dict.pop(serial_num)
        print(my_inventory_item_dict)
        return {"msg":"Successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found : " + serial_num)

# 6) Create 'GET' APIs (all items saved)   
@app.get("/items/")
def get_items() -> List[InventoryItem]:
    return my_inventory_item_dict.values()

