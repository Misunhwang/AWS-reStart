from dto import InventoryItem, ItemOrigin

def main():
    item_origin = ItemOrigin(country="Ethiopia", production_date="02/12/2023")

    # 1. DCO : Data Classes Object
    my_item1 = InventoryItem(name="printer", 
                             quantity=5, 
                             serial_num="HOUEHSK",
                             origin=item_origin)

    # 2. DCO -> JSON (serialized)
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1) 

    # 3. Json -> DCO (parsing)
    my_item2 = InventoryItem(**my_serialized_object1)
    print(my_item2.__dict__) 
        
if __name__ == "__main__":
    main()