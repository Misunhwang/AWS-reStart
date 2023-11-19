from fastapi.testclient import TestClient

from main import app
import pytest

@pytest.fixture
def client():
    yield TestClient(app)

# to use GET/DELETE API, PUT api needs to get used first - code repetition
# 1) fixture - precondition to test case. Pre-initialization of an object and return it
# 2) Providing a matrix of inputs and receiving a matrix of outputs
# 3) Mock - blackbox testing



@pytest.fixture
def good_payload():
    return {
        "name": "book1",
        "quantity": 3,
        "serial_num": "10ok",
        "origin": {"country": "Ethiopia", "production_date": "13/11/2023"},
    }


@pytest.fixture
def bad_payload():
    return {
        "name": "book2",
        "quantity": 5,
        "serial_num": "20ok",
        "origin": {"country": "Ethiopia", "production_date": "13/11/2023"},
    }


def test_put_api_422(bad_payload):
    print("\n----- Test PUT API with incorrect format -----\n")
    response = client.put("/items/20ok", json=bad_payload)

    assert response.status_code == 422


@pytest.fixture
def create_and_delete_item(good_payload):
    client.put("/items/20ok", json=good_payload)
    yield "Item created"
    client.delete(f"/items/20ok/{good_payload.serial_num}")
    
def test_get_item()
