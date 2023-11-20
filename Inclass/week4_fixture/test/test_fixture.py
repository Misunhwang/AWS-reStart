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
        "serial_num": "test",
        "origin": {"country": "Ethiopia", "production_date": "13/11/2023"},
    }


@pytest.fixture
def bad_payload():
    return {
        "name": "book2",
        "quantity": 5,
        "serial_num": "test",
        "origin": {"country": "Korea", "production_date": "13/11/2023"},
    }


"""
def test_create_and_delete_item(client, good_payload):
    client.get("/items/test/", json=good_payload)
    yield "Item Created"
    response = client.delete(f"/items/test/{good_payload.serial_num}")
    print(response.status_code)
"""


def test_bad_api(client, bad_payload):
    print("\n----- Test PUT API with incorrect format -----\n")
    response = client.put("/items/test/", json=bad_payload)
    assert response.status_code == 422


def test_get_api(client):
    response = client.get("/items/test/")
    assert response.status_code == 404


def test_put_then_get_api(client, good_payload):
    response = client.put("items/test/", json=good_payload)
    assert response.status_code == 200
    response = client.get("/items/test/")
    assert response.status_code == 200 and response.json() == good_payload


# parametrize
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),  # a=1, b=2, expected=3
        (5, -1, 4),  # a=5, b=-1, expected=4
        (3, 3, 6),
    ],
)
def test_addition(a, b, expected):
    assert a + b == expected


# parametrize allows to put thru many test cases at once, include parameter names as strings
# first test case a = 1, b = 2, expected = 3
# second test case a = 5, b = -1, expected = 4
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (5, -1, 4), (3, 3, 6)],
)
def test_addition(a, b, expected):
    assert a + b == expected


# @pytest.fixture
@pytest.mark.parametrize(
    "payload, http_code",
    [
        (
            {
                "name": "book1",
                "quantity": 3,
                "serial_num": "test",
                "origin": {"country": "Ethiopia", "production_date": "13/11/2023"},
            },
            200,
        ),
        (
            {
                "name": "book1",
                "quantity": 3,
                "serial_num": "test",
                "origin": {"country": "Korea", "production_date": "13/11/2023"},
            },
            422,
        ),
    ],  # indirect = ["payload"],
)
def test_many_put_apis(client, payload, http_code):
    assert client.put("items/test/", json=payload).status_code == http_code
