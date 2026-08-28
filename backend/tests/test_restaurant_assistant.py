from AI import restaurant_assistant
from fastapi.testclient import TestClient
from main import app
from AI.restaurant_tools import build_tool_registry

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

def test_order_overview_tool(db_session):
    product_response = client.post(
        "/products",
        json={
            "name": "AI Tool Pizza",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "AI-TOOL-001",
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

    tools = build_tool_registry(db_session)

    result = tools["get_order_overview"](
        order_id=order_id
    )

    assert result["order_id"] == order_id
    assert result["order_number"] == "AI-TOOL-001"
    assert result["total_amount"] == 20.0
    assert result["payment_status"] == "No payment"


def test_low_stock_tool(db_session):
    client.post(
        "/inventory",
        json={
            "item_name": "Test Mozzarella",
            "item_type": "ingredient",
            "current_quantity": 2,
            "minimum_quantity": 5,
            "unit": "kg"
        }
    )

    tools = build_tool_registry(db_session)

    result = tools["get_low_stock_items"]()

    assert len(result["items"]) == 1
    assert result["items"][0]["name"] == "Test Mozzarella"
    assert result["items"][0]["current_quantity"] == 2
    assert result["items"][0]["minimum_quantity"] == 5

def test_pending_payments_tool(db_session):
    product_response = client.post(
        "/products",
        json={
            "name": "Pending Tool Pizza",
            "price": 9.0
        }
    )

    product_id = product_response.json()["id"]

    client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "PENDING-TOOL-001",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 1
                }
            ]
        }
    )

    tools = build_tool_registry(db_session)

    result = tools["get_pending_payment_orders"]()

    assert len(result["orders"]) == 1
    assert result["orders"][0]["order_number"] == "PENDING-TOOL-001"
    assert result["orders"][0]["total_amount"] == 9.0

def test_kitchen_orders_tool(db_session):
    product_response = client.post(
        "/products",
        json={
            "name": "Kitchen Tool Pizza",
            "price": 12.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "KITCHEN-TOOL-001",
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

    client.patch(
        f"/kitchen/orders/{order_id}/status",
        params={
            "status": "Preparing"
        }
    )

    tools = build_tool_registry(db_session)

    result = tools["get_kitchen_orders"]()

    assert len(result["orders"]) == 1
    assert result["orders"][0]["order_number"] == "KITCHEN-TOOL-001"
    assert result["orders"][0]["order_status"] == "Preparing"
    assert result["orders"][0]["total_amount"] == 12.0

def test_notifications_tool(db_session):
    client.post(
        "/notifications",
        json={
            "customer_id": 1,
            "type": "order_status",
            "message": "Test notifikácia"
        }
    )

    tools = build_tool_registry(db_session)

    result = tools["get_notifications"]()

    assert len(result["notifications"]) == 1
    assert result["notifications"][0]["message"] == "Test notifikácia"
    assert result["notifications"][0]["status"] == "Pending"

def test_sales_report_tool(db_session):
    product_response = client.post(
        "/products",
        json={
            "name": "Sales Tool Pizza",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "SALES-TOOL-001",
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

    client.patch(
        f"/kitchen/orders/{order_id}/status",
        params={
            "status": "Ready"
        }
    )

    tools = build_tool_registry(db_session)

    result = tools["get_sales_report"]()

    assert result["total_revenue"] == 20.0
    assert result["completed_orders"] == 1
    assert result["total_items_sold"] == 2
    assert result["top_products"][0]["product_name"] == "Sales Tool Pizza"

def test_products_tool(db_session):
    client.post(
        "/products",
        json={
            "name": "Products Tool Pizza",
            "price": 8.5
        }
    )

    tools = build_tool_registry(db_session)

    result = tools["get_products"]()

    assert len(result["products"]) == 1
    assert result["products"][0]["name"] == "Products Tool Pizza"
    assert result["products"][0]["price"] == 8.5

def test_inventory_tool(db_session):
    client.post(
        "/inventory",
        json={
            "item_name": "Inventory Tool Mozzarella",
            "item_type": "ingredient",
            "current_quantity": 3,
            "minimum_quantity": 4,
            "unit": "kg"
        }
    )

    tools = build_tool_registry(db_session)

    result = tools["get_inventory"]()

    assert len(result["items"]) == 1
    assert result["items"][0]["name"] == "Inventory Tool Mozzarella"
    assert result["items"][0]["current_quantity"] == 3
    assert result["items"][0]["minimum_quantity"] == 4
    assert result["items"][0]["unit"] == "kg"