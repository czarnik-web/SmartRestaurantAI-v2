from services import (
    products_service,
    orders_service,
    payments_service,
    reporting_service,
    kitchen_service,
    notifications_service,
    inventory_service,
)


def build_tool_registry(db):
    def get_restaurant_status():
        """Získa aktuálny stav reštaurácie, tržby, objednávky a refundácie."""
        daily = reporting_service.get_daily_report(db)
        refunds = reporting_service.get_refund_report(db)

        return {
            "order_count": daily["order_count"],
            "total_revenue": daily["total_revenue"],
            "refund_count": refunds["refund_count"],
            "total_refunded": refunds["total_refunded"],
        }

    def get_product_count():
        """Zistí počet produktov alebo jedál evidovaných v systéme."""
        products = products_service.get_all_products(db)

        return {
            "product_count": len(products)
        }

    def get_order_overview(order_id: int):
        """Získa informácie o konkrétnej objednávke podľa jej ID."""
        order = orders_service.get_order_by_id(db, order_id)

        if order is None:
            return {
                "error": "Objednávka nebola nájdená."
            }

        payment = payments_service.get_payment_by_order_id(
            db,
            order_id
        )

        return {
            "order_id": order.id,
            "order_number": order.order_number,
            "order_status": order.order_status,
            "total_amount": order.total_amount,
            "payment_status": (
                payment.status
                if payment is not None
                else "No payment"
            ),
        }

    def get_low_stock_items():
        """Zistí, ktoré skladové položky sú na alebo pod minimálnym množstvom."""
        daily = reporting_service.get_daily_report(db)

        return {
            "items": [
                {
                    "name": item.item_name,
                    "current_quantity": item.current_quantity,
                    "minimum_quantity": item.minimum_quantity,
                    "unit": item.unit,
                }
                for item in daily["low_stock_items"]
            ]
        }

    def get_pending_payment_orders():
        """Zistí objednávky, ktoré ešte čakajú na platbu."""
        orders = orders_service.get_all_orders(db)

        pending_orders = [
            order
            for order in orders
            if order.payment_status == "Pending"
        ]

        return {
            "orders": [
                {
                    "id": order.id,
                    "order_number": order.order_number,
                    "total_amount": order.total_amount,
                }
                for order in pending_orders
            ]
        }

    def get_kitchen_orders():
        """Získa objednávky, ktoré sú aktuálne v kuchyni alebo čakajú na prípravu."""
        orders = kitchen_service.get_all_kitchen_orders(db)

        active_orders = [
            order
            for order in orders
            if order.order_status in ["New", "Preparing"]
        ]

        return {
            "orders": [
                {
                    "id": order.id,
                    "order_number": order.order_number,
                    "order_status": order.order_status,
                    "total_amount": order.total_amount,
                }
                for order in active_orders
            ]
        }

    def get_notifications():
        """Získa notifikácie evidované v systéme, najmä čakajúce na spracovanie."""
        notifications = notifications_service.get_all_notifications(db)

        return {
            "notifications": [
            {
                "id": notification.id,
                "customer_id": notification.customer_id,
                "type": notification.type,
                "message": notification.message,
                "status": notification.status,
            }
            for notification in notifications
        ]
    }

    def get_sales_report():
        """Získa prehľad tržieb, dokončených objednávok, predaných položiek a top produktov."""
        report = reporting_service.get_sales_report(db)

        return {
            "total_revenue": report["total_revenue"],
            "completed_orders": report["completed_orders"],
            "total_items_sold": report["total_items_sold"],
            "top_products": report["top_products"],
        }

    def get_products():
        """Získa zoznam produktov alebo jedál vrátane ich ID, názvu a ceny."""
        products = products_service.get_all_products(db)

        return {
            "products": [
                {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                }
                for product in products
            ]
        }

    def get_inventory():
        """Získa aktuálny obsah skladu vrátane množstva, minima, jednotky a stavu."""
        items = inventory_service.get_all_inventory_items(db)

        return {
            "items": [
                {
                    "id": item.id,
                    "name": item.item_name,
                    "type": item.item_type,
                    "current_quantity": item.current_quantity,
                    "minimum_quantity": item.minimum_quantity,
                    "unit": item.unit,
                    "status": item.status,
                }
                for item in items
            ]
        }

    return {
        "get_restaurant_status": get_restaurant_status,
        "get_product_count": get_product_count,
        "get_order_overview": get_order_overview,
        "get_low_stock_items": get_low_stock_items,
        "get_pending_payment_orders": get_pending_payment_orders,
        "get_kitchen_orders": get_kitchen_orders,
        "get_notifications": get_notifications,
        "get_sales_report": get_sales_report,
        "get_products": get_products,
        "get_inventory": get_inventory,
    }

