from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_payment_uses_order_total_amount():
    product_response = client.post(
        "/products",
        json={
            "name": "Test Burger",
            "price": 8.50
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "PAY-TEST-001",
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

    order_id = order_response.json()["id"]

    payment_response = client.post(
        "/payments",
        json={
            "order_id": order_id,
            "payment_method": "card"
        }
    )

    assert payment_response.status_code == 200

    payment = payment_response.json()

    assert payment["order_id"] == order_id
    assert payment["amount"] == 17.0
    assert payment["status"] == "Pending"

def test_order_cannot_have_two_payments():
    product_response = client.post(
        "/products",
        json={
            "name": "Test Pasta",
            "price": 12.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "PAY-TEST-002",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 1
                }
            ]
        }
    )

    order_id = order_response.json()["id"]

    first_payment = client.post(
        "/payments",
        json={
            "order_id": order_id,
            "payment_method": "card"
        }
    )

    assert first_payment.status_code == 200

    second_payment = client.post(
        "/payments",
        json={
            "order_id": order_id,
            "payment_method": "card"
        }
    )

    assert second_payment.status_code == 409
    assert second_payment.json() == {
        "detail": "Platba pre túto objednávku už existuje"
    }

def test_payment_status_syncs_to_order():
    product_response = client.post(
        "/products",
        json={
            "name": "Test Pizza Sync",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "PAY-TEST-003",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 1
                }
            ]
        }
    )

    order_id = order_response.json()["id"]

    payment_response = client.post(
        "/payments",
        json={
            "order_id": order_id,
            "payment_method": "card"
        }
    )

    payment_id = payment_response.json()["id"]

    update_response = client.patch(
        f"/payments/{payment_id}",
        json={
            "status": "Paid"
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["status"] == "Paid"

    order_response = client.get(f"/orders/{order_id}")

    assert order_response.status_code == 200
    assert order_response.json()["payment_status"] == "Paid"