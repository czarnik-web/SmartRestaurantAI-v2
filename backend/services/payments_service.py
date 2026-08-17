import models


def get_all_payments(db):
    return db.query(models.Payment).all()

def get_payment_by_id(db, payment_id: int):
    return (
        db.query(models.Payment)
        .filter(models.Payment.id == payment_id)
        .first()
    )

def create_payment(db, payment):
    new_payment = models.Payment(
        order_id=payment.order_id,
        payment_method=payment.payment_method,
        amount=payment.amount
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment

def update_payment(db, payment_id: int, payment_update):
    payment = get_payment_by_id(db, payment_id)

    if payment is None:
        return None

    if payment_update.status is not None:
        payment.status = payment_update.status

        order = (
            db.query(models.Order)
            .filter(models.Order.id == payment.order_id)
            .first()
        )

        if order is not None:
            order.payment_status = payment_update.status

    db.commit()
    db.refresh(payment)

    return payment