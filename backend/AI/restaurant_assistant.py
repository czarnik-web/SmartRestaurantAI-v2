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
    intent = detect_intent(message)

    if intent == "restaurant_status":
        status = get_restaurant_status(db)

        return (
            f"Objednávky: {status['daily']['order_count']}, "
            f"tržby: {status['daily']['total_revenue']} €, "
            f"refundácie: {status['refunds']['refund_count']}."
        )

    if intent == "product_count":
        products = get_products(db)

        return f"V systéme máme {len(products)} produktov."

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