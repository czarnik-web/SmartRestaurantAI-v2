import json
from services import (
    products_service,
    orders_service,
    payments_service,
    inventory_service,
    kitchen_service,
    notifications_service,
    reporting_service,
)
from AI.ollama_client import ask_ollama



def get_products(db):
    return products_service.get_all_products(db)


def get_order_overview(db, order_id: int):
    order = orders_service.get_order_by_id(db, order_id)

    if order is None:
        return None

    payment = payments_service.get_payment_by_order_id(
        db,
        order_id
    )

    return {
        "order": order,
        "payment": payment
    }


def get_restaurant_status(db):
    daily_report = reporting_service.get_daily_report(db)
    sales_report = reporting_service.get_sales_report(db)
    refund_report = reporting_service.get_refund_report(db)

    return {
        "daily": daily_report,
        "sales": sales_report,
        "refunds": refund_report
    }

def process_message(db, message: str):
    decision = detect_action(message)

    action = decision.get("action")

    if action == "restaurant_status":
        status = get_restaurant_status(db)

        return (
            f"Objednávky: {status['daily']['order_count']}, "
            f"tržby: {status['daily']['total_revenue']} €, "
            f"refundácie: {status['refunds']['refund_count']}."
        )

    if action == "product_count":
        products = get_products(db)

        return f"V systéme máme {len(products)} produktov."

    if action == "order_overview":
        order_id = decision.get("order_id")

        if order_id is None:
            return "Chýba ID objednávky."

        overview = get_order_overview(db, order_id)

        if overview is None:
            return f"Objednávka {order_id} nebola nájdená."

        order = overview["order"]
        payment = overview["payment"]

        payment_status = (
            payment.status
            if payment is not None
            else "Platba zatiaľ neexistuje"
        )

        return (
            f"Objednávka {order.order_number}: "
            f"stav {order.order_status}, "
            f"suma {order.total_amount} €, "
            f"platba {payment_status}."
        )

    return "Tejto požiadavke zatiaľ nerozumiem."

def detect_intent(message: str):
    prompt = f"""
Urči zámer používateľa v systéme Smart Restaurant AI.

Povolené zámery:
- restaurant_status
- product_count
- unknown

Odpovedz iba jedným z týchto názvov.
Žiadne vysvetlenie.

Správa používateľa:
{message}
"""

    intent = ask_ollama(prompt)

    return intent.strip()

def detect_action(message: str):
    prompt = f"""
Si rozhodovacia vrstva systému Smart Restaurant AI.

Vyber jednu povolenú akciu:

- restaurant_status
- product_count
- order_overview
- unknown

Akcia order_overview potrebuje order_id.

Odpovedz IBA platným JSON objektom.
Nepoužívaj markdown ani vysvetlenie.

Príklady:

{{"action": "restaurant_status"}}

{{"action": "product_count"}}

{{"action": "order_overview", "order_id": 2}}

{{"action": "unknown"}}

Správa používateľa:
{message}
"""

    result = ask_ollama(prompt)

    try:
        decision = json.loads(result.strip())
    except json.JSONDecodeError:
        return {"action": "unknown"}

    if not isinstance(decision, dict):
        return {"action": "unknown"}

    return decision

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