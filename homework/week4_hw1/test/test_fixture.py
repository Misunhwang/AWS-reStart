# 1) Convert into test fixture
from fastapi.testclient import TestClient
import pytest

from main import app


print("\n----- 1) Convert into test fixture -----\n")


@pytest.fixture
def client():
    yield TestClient(app)


@pytest.fixture
def good_payload():
    return {
        "name": "Table",
        "quantity": 5,
        "serial_num": "5table",
        "origin": {"country": "Ethiopia", "production_date": "13/11/2023"},
    }


@pytest.fixture
def bad_payload():
    return {
        "name": "Shelf",
        "quantity": 10,
        "serial_num": "10shelf",
        "origin": {"country": "Korea", "production_date": "7/1/2000"},
    }


@pytest.fixture
def good_other_payload():
    return {
        "name": "Chair",
        "quantity": 70,
        "serial_num": "70chair",
        "origin": {"country": "Ethiopia", "production_date": "25/12/2022"},
    }


# 2) Test PUT API with correct format
def test_put_api_200(client, good_payload):
    print("\n----- 2) Test PUT API with correct format -----\n")
    response = client.put(
        "/items/5table",
        json=good_payload,
    )

    print("\nStatus code : ", response.status_code)
    print("response.json() : ", response.json())
    assert response.status_code == 200


# 3) Test PUT API with incorrect format
def test_put_api_422(client, bad_payload):
    print("\n----- 3) Test PUT API with incorrect format -----\n")
    response = client.put(
        "/items/10shelf",
        json=bad_payload,
    )

    print("\nStatus code : ", response.status_code)
    print("response.json() : ", response.json())
    assert response.status_code == 422


# 4) Test GET API and compare Put & Get
def test_get_api(client, good_other_payload):
    print("\n----- 4) Test GET API and compare Put & Get -----\n")
    response_put = client.put(
        "/items/70chair",
        json=good_other_payload,
    )

    assert response_put.status_code == 200
    response_get = client.get("/items/70chair")

    try:
        assert response_get.status_code == 200 and response_get.json() == good_payload
    except AssertionError as ae:
        print("AssertionError happened!")
    else:
        print("PUT and GET is same")


# 5) Test DELETE API & Check Item deleted
def test_delete_api_404(client):
    print("\n----- 5) Test DELETE API & Check Item deleted -----\n")

    client.delete("/items/70chair")

    response = client.get("/items/70chair")

    print("\nStatus code : ", response.status_code)
    print("response.json() : ", response.json())
    assert response.status_code == 404


# 6) Test GET ALL API
def test_get_all_api(client):
    print("\n----- 6) Test GET ALL API -----\n")
    response = client.get("/items/")

    print("\nStatus code : ", response.status_code)
    print("response.json() : ", response.json())
    assert response.status_code == 200


@pytest.mark.parametrize(
    "serial_num, payload, http_code",
    [
        (
            "5table",
            {
                "name": "Table",
                "quantity": 5,
                "serial_num": "5table",
                "origin": {"country": "Ethiopia", "production_date": "13/11/2023"},
            },
            200,
        ),
        (
            "70chair",
            {
                "name": "Chair",
                "quantity": 70,
                "serial_num": "70chair",
                "origin": {"country": "Ethiopia", "production_date": "25/12/2022"},
            },
            404,
        ),
    ],
)
def test_many_put_apis(client, serial_num, payload, http_code):
    print("\n----- 7) Use parametrize() to test GET API -----\n")
    assert client.get(f"items/{serial_num}").status_code == http_code


@pytest.mark.parametrize(
    "payload, http_code",
    [
        (
            {
                "name": "Desk",
                "quantity": 5,
                "serial_num": "20desk",
                "origin": {"country": "Ethiopia", "production_date": "1/1/2000"},
            },
            200,
        ),
    ],
)
def test_compare_apis(client, payload, http_code):
    print("\n----- 8) Use parametrize() to compare GET API -----\n")
    response = client.put("items/20desk/", json=payload)
    assert response.status_code == http_code
    response = client.get("/items/20desk/")
    assert response.status_code == http_code and response.json() == payload
