# pytest

from fastapi.testclient import TestClient
#from fastapi import FastAPI, HTTPException

from main import app


# Look for file names with test_*.py
#def test_*():
#    pass
#test_*.py

# unit tests
"""
install 'pytest' : pip install pytest
> python -m pytest
> python -m pytest -vvl
"""
def test_basic_example():
    # pass
    assert(True)

client = TestClient(app)

def test_put_api():
    response = client.put("/items/10ok", json = {
        "name": "book2",
        "quantity": 5,
        "serial_num": "10ok",
        "origin": {
            "country": "Ethiopia",
            "production_date": "13/11/2023"        
        }
    })

    print(response.json())
    assert response.status_code == 200
