import models


def get_all_orders(db):
    return db.query(models.Order).all()

def get_order_by_id(db, order_id: int):
    return (
        db.query(models.Order)
        .filter(models.Order.id == order_id)
        .first()
    )

def get_order_by_number(db, order_number: str):
    return (
        db.query(models.Order)
        .filter(models.Order.order_number == order_number)
        .first()
    )

def create_order(db, order):
    new_order = models.Order(
        customer_id=order.customer_id,
        order_number=order.order_number,
        order_type=order.order_type,
        total_amount=0.0
    )

    db.add(new_order)
    db.flush()

    total_amount = 0.0

    for item in order.items:
        product = (
            db.query(models.Product)
            .filter(models.Product.id == item.product_id)
            .first()
        )

        if product is None:
            db.rollback()
            return None

        new_item = models.OrderItem(
            order_id=new_order.id,
            product_id=product.id,
            quantity=item.quantity,
            unit_price=product.price
        )

        total_amount += product.price * item.quantity

        db.add(new_item)

    new_order.total_amount = total_amount

    db.commit()
    db.refresh(new_order)

    return new_order

def update_order(db, order_id: int, order_update):
    order = get_order_by_id(db, order_id)

    if order is None:
        return None

    if order_update.order_status is not None:
        order.order_status = order_update.order_status


    db.commit()
    db.refresh(order)

    return order