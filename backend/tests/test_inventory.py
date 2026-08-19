from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_inventory_quantity_cannot_be_negative():
    response = client.post(
        "/inventory",
        json={
            "item_name": "Test Mozzarella",
            "item_type": "ingredient",
            "current_quantity": -5,
            "minimum_quantity": 2,
            "unit": "kg"
        }
    )

    assert response.status_code == 422

def test_create_and_update_inventory_item():
    create_response = client.post(
        "/inventory",
        json={
            "item_name": "Test Syr",
            "item_type": "ingredient",
            "current_quantity": 10,
            "minimum_quantity": 3,
            "unit": "kg"
        }
    )

    assert create_response.status_code == 200

    item_id = create_response.json()["id"]

    update_response = client.patch(
        f"/inventory/{item_id}",
        json={
            "current_quantity": 5
        }
    )

    assert update_response.status_code == 200
    assert update_response.json()["current_quantity"] == 5