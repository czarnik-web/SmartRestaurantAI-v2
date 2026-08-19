from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_create_and_get_notification():
    create_response = client.post(
        "/notifications",
        json={
            "customer_id": 1,
            "type": "order_status",
            "message": "Objednávka je pripravená."
        }
    )

    assert create_response.status_code == 200

    notification = create_response.json()

    assert notification["customer_id"] == 1
    assert notification["type"] == "order_status"
    assert notification["message"] == "Objednávka je pripravená."
    assert notification["status"] == "Pending"

    notification_id = notification["id"]

    get_response = client.get(
        f"/notifications/{notification_id}"
    )

    assert get_response.status_code == 200
    assert get_response.json()["id"] == notification_id