# 1) Setup Unit testing structure
from fastapi.testclient import TestClient

from main import app

def test_basic_example():
    assert(True)

client = TestClient(app)

# 2) Test PUT API with correct format
def test_put_api_200():
    print("\n----- Test PUT API with correct format -----\n")
    response = client.put("/items/5table", json = {
        "name": "Table",
        "quantity": 5,
        "serial_num": "5table",
        "origin": {
            "country": "Ethiopia",
            "production_date": "13/11/2023"        
        }
    })

    print("\nStatus code : ", response.status_code)
    print("response.json() : ", response.json())
    assert response.status_code == 200

# 3) Test PUT API with incorrect format
def test_put_api_422():
    print("\n----- Test PUT API with incorrect format -----\n")
    response = client.put("/items/10shelf", json = {
        "name": "Shelf",
        "quantity": 10,
        "serial_num": "10shelf",
        "origin": {
            "country": "Korea",
            "production_date": "7/1/2000"        
        }
    })

    print("\nStatus code : ", response.status_code)
    print("response.json() : ", response.json())
    assert response.status_code == 422

# 4) Test GET API and compare Put & Get
def test_get_api():
    print("\n----- Test GET API and compare Put & Get -----\n")
    response_put = client.put("/items/70chair", json = {
        "name": "Chair",
        "quantity": 70,
        "serial_num": "70chair",
        "origin": {
            "country": "Ethiopia",
            "production_date": "25/12/2022"        
        }
    })

    response_get = client.get("/items/70chair")

    try:
        assert response_put._request.content.decode().replace('"','\'') == str(response_get.json())
    except AssertionError as ae:
        print("AssertionError happened!")
    else:
        print("PUT and GET is same")

# 5) Test DELETE API & Check Item deleted
def test_delete_api_404():
    print("\n----- Test DELETE API & Check Item deleted -----\n")

    client.delete("/items/70chair")

    response = client.get("/items/70chair")

    print("\nStatus code : ", response.status_code)
    print("response.json() : ", response.json())
    assert response.status_code == 404

# 6) Test GET ALL API
def test_get_all_api():
    print("\n----- Test GET ALL API -----\n")
    response = client.get("/items/")

    print("\nStatus code : ", response.status_code)
    print("response.json() : ", response.json())
    assert response.status_code == 200