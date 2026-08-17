from fastapi import APIRouter, HTTPException, Depends

import schemas

from database import SessionLocal
from services import payments_service


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[schemas.PaymentResponse])
def get_payments(db=Depends(get_db)):
    return payments_service.get_all_payments(db)

@router.get("/{id}", response_model=schemas.PaymentResponse)
def get_payment(id: int, db=Depends(get_db)):
    payment = payments_service.get_payment_by_id(db, id)

    if payment is None:
        raise HTTPException(status_code=404, detail="Platba nebola nájdená")

    return payment

@router.post("", response_model=schemas.PaymentResponse)
def create_payment(payment: schemas.PaymentCreate, db=Depends(get_db)):
    return payments_service.create_payment(db, payment)

@router.patch("/{id}", response_model=schemas.PaymentResponse)
def update_payment(
    id: int,
    payment_update: schemas.PaymentUpdate,
    db=Depends(get_db)
):
    payment = payments_service.update_payment(db, id, payment_update)

    if payment is None:
        raise HTTPException(status_code=404, detail="Platba nebola nájdená")

    return payment