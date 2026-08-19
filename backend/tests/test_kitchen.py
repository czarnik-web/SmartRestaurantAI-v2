from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_kitchen_can_update_order_status():
    product_response = client.post(
        "/products",
        json={
            "name": "Kitchen Test Pizza",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "KITCHEN-TEST-001",
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

    response = client.patch(
        f"/kitchen/orders/{order_id}/status",
        params={
            "status": "Ready"
        }
    )

    assert response.status_code == 200
    assert response.json()["order_status"] == "Ready"

def test_kitchen_rejects_invalid_status():
    product_response = client.post(
        "/products",
        json={
            "name": "Kitchen Invalid Test",
            "price": 9.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "KITCHEN-TEST-002",
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

    response = client.patch(
        f"/kitchen/orders/{order_id}/status",
        params={
            "status": "Banana"
        }
    )

    assert response.status_code == 422