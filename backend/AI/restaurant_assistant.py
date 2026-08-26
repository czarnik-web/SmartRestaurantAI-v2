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

    if action == "low_stock":
        items = get_low_stock_items(db)

        if not items:
            return "Momentálne nemáme žiadne skladové položky pod minimálnym množstvom."

        item_names = ", ".join(
            item.item_name
            for item in items
        )

        return f"Nízky stav skladu majú položky: {item_names}."

    if action == "pending_payments":
        orders = get_pending_payment_orders(db)

        if not orders:
            return "Momentálne nemáme žiadne objednávky čakajúce na platbu."

        order_numbers = ", ".join(
            order.order_number
            for order in orders
        )

        return (
            f"Na platbu čakajú objednávky: "
            f"{order_numbers}."
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
- low_stock
- pending_payments

Akcia order_overview potrebuje order_id.

Odpovedz IBA platným JSON objektom.
Nepoužívaj markdown ani vysvetlenie.

Príklady:

{{"action": "restaurant_status"}}

{{"action": "product_count"}}

{{"action": "order_overview", "order_id": 2}}

{{"action": "unknown"}}

{{"action": "low_stock"}}

{{"action": "pending_payments"}}

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

def get_low_stock_items(db):
    daily_report = reporting_service.get_daily_report(db)

    return daily_report["low_stock_items"]

def get_pending_payment_orders(db):
    orders = orders_service.get_all_orders(db)

    return [
        order
        for order in orders
        if order.payment_status == "Pending"
    ]