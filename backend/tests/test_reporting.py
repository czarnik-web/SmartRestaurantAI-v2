from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_daily_report():
    product_response = client.post(
        "/products",
        json={
            "name": "Reporting Test Pizza",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "REPORT-TEST-001",
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

    report_response = client.get("/reports/daily")

    assert report_response.status_code == 200

    report = report_response.json()

    assert report["order_count"] == 1
    assert report["total_revenue"] == 20.0

def test_sales_report():
    product_response = client.post(
        "/products",
        json={
            "name": "Sales Test Pizza",
            "price": 12.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "SALES-TEST-001",
            "order_type": "takeaway",
            "items": [
                {
                    "product_id": product_id,
                    "quantity": 3
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

    report_response = client.get("/reports/sales")

    assert report_response.status_code == 200

    report = report_response.json()

    assert report["total_revenue"] == 36.0
    assert report["completed_orders"] == 1
    assert report["total_items_sold"] == 3

    assert report["top_products"][0]["product_id"] == product_id
    assert report["top_products"][0]["product_name"] == "Sales Test Pizza"
    assert report["top_products"][0]["quantity_sold"] == 3

def test_refund_report():
    product_response = client.post(
        "/products",
        json={
            "name": "Refund Test Pizza",
            "price": 10.0
        }
    )

    product_id = product_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "customer_id": 1,
            "order_number": "REFUND-TEST-001",
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

    client.patch(
        f"/payments/{payment_id}",
        json={
            "status": "Refunded"
        }
    )

    report_response = client.get("/reports/refunds")

    assert report_response.status_code == 200

    report = report_response.json()

    assert report["refund_count"] == 1
    assert report["total_refunded"] == 10.0