import models


def get_daily_report(db):
    order_count = db.query(models.Order).count()

    paid_payments = (
        db.query(models.Payment)
        .filter(models.Payment.status == "Paid")
        .all()
    )

    total_revenue = sum(payment.amount for payment in paid_payments)

    low_stock_items = (
        db.query(models.InventoryItem)
        .filter(
            models.InventoryItem.current_quantity
            <= models.InventoryItem.minimum_quantity
        )
        .all()
    )

    return {
        "order_count": order_count,
        "total_revenue": total_revenue,
        "low_stock_items": low_stock_items
    }

def get_sales_report(db):
    paid_payments = (
        db.query(models.Payment)
        .filter(models.Payment.status == "Paid")
        .all()
    )

    total_revenue = sum(payment.amount for payment in paid_payments)

    paid_order_ids = {
        payment.order_id for payment in paid_payments
    }

    completed_orders = (
        db.query(models.Order)
        .filter(models.Order.order_status == "Ready")
        .count()
    )

    if paid_order_ids:
        order_items = (
            db.query(models.OrderItem)
            .filter(models.OrderItem.order_id.in_(paid_order_ids))
            .all()
        )
    else:
        order_items = []

    total_items_sold = sum(item.quantity for item in order_items)

    product_totals = {}

    for item in order_items:
        product_totals[item.product_id] = (
            product_totals.get(item.product_id, 0) + item.quantity
        )

    top_products = []

    for product_id, quantity_sold in product_totals.items():
        product = (
            db.query(models.Product)
            .filter(models.Product.id == product_id)
            .first()
        )

        if product is not None:
            top_products.append({
                "product_id": product.id,
                "product_name": product.name,
                "quantity_sold": quantity_sold
            })

    top_products.sort(
        key=lambda product: product["quantity_sold"],
        reverse=True
    )

    return {
        "total_revenue": total_revenue,
        "completed_orders": completed_orders,
        "total_items_sold": total_items_sold,
        "top_products": top_products[:3]
    }

def get_refund_report(db):
    refunded_payments = (
        db.query(models.Payment)
        .filter(models.Payment.status == "Refunded")
        .all()
    )

    refund_count = len(refunded_payments)

    total_refunded = sum(
        payment.amount for payment in refunded_payments
    )

    return {
        "refund_count": refund_count,
        "total_refunded": total_refunded
    }