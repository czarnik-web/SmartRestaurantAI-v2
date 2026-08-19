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

def test_order_with_nonexistent_product_returns_404():
    response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "TEST-NOT-FOUND",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": 999,
                    "quantity": 1
                }
            ]
        }
    )

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Produkt nebol nájdený"
    }

def test_duplicate_order_number_returns_409():
    product_response = client.post(
        "/products",
        json={
            "name": "Duplicate Order Test Product",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_data = {
        "customer_id": 1,
        "order_number": "DUPLICATE-001",
        "order_type": "takeaway",
        "items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ]
    }

    first_response = client.post(
        "/orders",
        json=order_data
    )

    assert first_response.status_code == 200

    second_response = client.post(
        "/orders",
        json=order_data
    )

    assert second_response.status_code == 409
    assert second_response.json() == {
        "detail": "Objednávka s týmto číslom už existuje"
    }

def test_get_nonexistent_order_returns_404():
    response = client.get("/orders/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Objednávka nebola nájdená"
    }