from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_create_and_get_product():
    create_response = client.post(
        "/products",
        json={
            "name": "Test Pizza",
            "price": 9.50
        }
    )

    assert create_response.status_code == 200

    created_product = create_response.json()

    assert created_product["name"] == "Test Pizza"
    assert created_product["price"] == 9.50

    product_id = created_product["id"]

    get_response = client.get(f"/products/{product_id}")

    assert get_response.status_code == 200

    product = get_response.json()

    assert product["id"] == product_id
    assert product["name"] == "Test Pizza"
    assert product["price"] == 9.50

def test_product_price_must_be_positive():
    response = client.post(
        "/products",
        json={
            "name": "Invalid Product",
            "price": -5
        }
    )

    assert response.status_code == 422