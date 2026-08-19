from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_create_order_calculates_total_amount():
    product_response = client.post(
        "/products",
        json={
            "name": "Pizza Test",
            "price": 10.50
        }
    )

    assert product_response.status_code == 200

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "TEST-001",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2
                }
            ]
        }
    )

    assert order_response.status_code == 200

    order = order_response.json()

    assert order["order_number"] == "TEST-001"
    assert order["total_amount"] == 21.0
    assert order["items"][0]["quantity"] == 2
    assert order["items"][0]["unit_price"] == 10.50

def test_order_quantity_must_be_positive():
    product_response = client.post(
        "/products",
        json={
            "name": "Pizza Test",
            "price": 10.50
        }
    )

    product_id = product_response.json()["id"]

    response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "TEST-INVALID",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": -2
                }
            ]
        }
    )

    assert response.status_code == 422