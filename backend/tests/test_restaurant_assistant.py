from AI import restaurant_assistant
from fastapi.testclient import TestClient
from main import app

from services import (
    products_service,
    orders_service,
    payments_service,
    inventory_service,
    kitchen_service,
    notifications_service,
    reporting_service,
)

client = TestClient(app)


def test_restaurant_assistant_gets_products(db_session):
    products = restaurant_assistant.get_products(db_session)

    assert isinstance(products, list)

def test_restaurant_assistant_gets_order_overview(db_session):
    product_response = client.post(
        "/products",
        json={
            "name": "Assistant Test Pizza",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "ASSISTANT-001",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2
                }
            ]
        }
    )

    order_id = order_response.json()["id"]

    client.post(
        "/payments",
        json={
            "order_id": order_id,
            "payment_method": "card"
        }
    )

    overview = restaurant_assistant.get_order_overview(
        db_session,
        order_id
    )

    assert overview is not None
    assert overview["order"].id == order_id
    assert overview["payment"].order_id == order_id
    assert overview["payment"].amount == 20.0

def get_restaurant_status(db):
    daily_report = reporting_service.get_daily_report(db)
    sales_report = reporting_service.get_sales_report(db)
    refund_report = reporting_service.get_refund_report(db)

    return {
        "daily": daily_report,
        "sales": sales_report,
        "refunds": refund_report
    }

def test_restaurant_assistant_gets_restaurant_status(db_session):
    product_response = client.post(
        "/products",
        json={
            "name": "Status Test Pizza",
            "price": 15.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "STATUS-001",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2
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

    client.patch(
        f"/payments/{payment_id}",
        json={
            "status": "Paid"
        }
    )

    status = restaurant_assistant.get_restaurant_status(
        db_session
    )

    assert "daily" in status
    assert "sales" in status
    assert "refunds" in status
    assert status["daily"]["order_count"] == 1
    assert status["daily"]["total_revenue"] == 30.0

def test_process_message_routes_to_order_overview(
    db_session,
    monkeypatch
):
    product_response = client.post(
        "/products",
        json={
            "name": "AI Routing Pizza",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "AI-ROUTE-001",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 2
                }
            ]
        }
    )

    order_id = order_response.json()["id"]

    monkeypatch.setattr(
        restaurant_assistant,
        "detect_action",
        lambda message: {
            "action": "order_overview",
            "order_id": order_id
        }
    )

    response = restaurant_assistant.process_message(
        db_session,
        "Ukáž mi túto objednávku"
    )

    assert "AI-ROUTE-001" in response
    assert "20.0 €" in response

def test_detect_action_handles_invalid_json(monkeypatch):
    monkeypatch.setattr(
        restaurant_assistant,
        "ask_ollama",
        lambda prompt: "toto nie je JSON"
    )

    decision = restaurant_assistant.detect_action(
        "Nejaká požiadavka"
    )

    assert decision == {
        "action": "unknown"
    }