import models


def get_all_orders(db):
    return db.query(models.Order).all()

def get_order_by_id(db, order_id: int):
    return (
        db.query(models.Order)
        .filter(models.Order.id == order_id)
        .first()
    )

def create_order(db, order):
    new_order = models.Order(
        customer_id=order.customer_id,
        order_number=order.order_number,
        order_type=order.order_type,
        total_amount=order.total_amount
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

def update_order(db, order_id: int, order_update):
    order = get_order_by_id(db, order_id)

    if order is None:
        return None

    if order_update.order_status is not None:
        order.order_status = order_update.order_status

    if order_update.payment_status is not None:
        order.payment_status = order_update.payment_status

    db.commit()
    db.refresh(order)

    return order