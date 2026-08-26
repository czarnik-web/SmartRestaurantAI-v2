
from services import (
    products_service,
    orders_service,
    payments_service,
    inventory_service,
    kitchen_service,
    notifications_service,
    reporting_service,
)
from AI.ollama_client import run_tool_chat
from AI.restaurant_tools import build_tool_registry



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
    tool_registry = build_tool_registry(db)

    return run_tool_chat(
        message,
        tool_registry
    )


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