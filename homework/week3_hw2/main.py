from pydantic import BaseModel, field_validator

class BookItem(BaseModel):
    name : str
    author : str

class ItemOrigin(BaseModel):
    country: str
    production_date: str
    
    @field_validator("country")
    @classmethod
    def check_valid_country(cls, country: str):
        assert country == "Ethiopia", "country name must be Ethiopia"
        return country

class InventoryItem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin


def main():
    item_origin = ItemOrigin(country="Ethiopia", production_date="02/12/2023")

    # 1. DCO : Data Classes Object
    my_item1 = InventoryItem(name="printer", 
                             quantity=5, 
                             serial_num="HOUEHSK",
                             origin=item_origin)
    #print(my_item1.__dict__)

    # 2. DCO -> JSON (serialized)
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1) # {'name': 'printer', 'quantity': 5, 'serial_num': 'HOUEHSK', 'origin': ItemOrigin(country='Ethiopian', production_data='02/12/2023')}

    # 3. Json -> DCO (parsing)
    my_item2 = InventoryItem(**my_serialized_object1)
    print(my_item2.__dict__) # {'name': 'printer', 'quantity': 5, 'serial_num': 'HOUEHSK', 'origin': ItemOrigin(country='Ethiopian', production_data='02/12/2023')}
    
if __name__ == "__main__":
    main()