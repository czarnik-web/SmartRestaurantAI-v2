from fastapi import APIRouter, HTTPException, Depends

import schemas

from database import SessionLocal
from services import notifications_service


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[schemas.NotificationResponse])
def get_notifications(db=Depends(get_db)):
    return notifications_service.get_all_notifications(db)

@router.get("/{id}", response_model=schemas.NotificationResponse)
def get_notification(id: int, db=Depends(get_db)):
    notification = notifications_service.get_notification_by_id(db, id)

    if notification is None:
        raise HTTPException(status_code=404, detail="Notifikácia nebola nájdená")

    return notification

@router.post("", response_model=schemas.NotificationResponse)
def create_notification(
    notification: schemas.NotificationCreate,
    db=Depends(get_db)
):
    return notifications_service.create_notification(db, notification)