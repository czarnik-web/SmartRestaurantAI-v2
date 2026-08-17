import models


def get_all_notifications(db):
    return db.query(models.Notification).all()

def get_notification_by_id(db, notification_id: int):
    return (
        db.query(models.Notification)
        .filter(models.Notification.id == notification_id)
        .first()
    )

def create_notification(db, notification):
    new_notification = models.Notification(
        customer_id=notification.customer_id,
        type=notification.type,
        message=notification.message
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification