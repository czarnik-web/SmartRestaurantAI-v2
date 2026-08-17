import models


def get_all_kitchen_orders(db):
    return db.query(models.Order).all()

def get_kitchen_order_by_id(db, order_id: int):
    return (
        db.query(models.Order)
        .filter(models.Order.id == order_id)
        .first()
    )

def update_kitchen_order_status(db, order_id: int, status: str):
    order = get_kitchen_order_by_id(db, order_id)

    if order is None:
        return None

    order.order_status = status

    db.commit()
    db.refresh(order)

    return order