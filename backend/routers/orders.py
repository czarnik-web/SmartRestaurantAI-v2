from fastapi import APIRouter, HTTPException, Depends

import schemas

from database import SessionLocal
from services import orders_service


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[schemas.OrderResponse])
def get_orders(db=Depends(get_db)):
    return orders_service.get_all_orders(db)

@router.get("/{id}", response_model=schemas.OrderResponse)
def get_order(id: int, db=Depends(get_db)):
    order = orders_service.get_order_by_id(db, id)

    if order is None:
        raise HTTPException(status_code=404, detail="Objednávka nebola nájdená")

    return order

@router.post("", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db=Depends(get_db)):
    return orders_service.create_order(db, order)

@router.patch("/{id}", response_model=schemas.OrderResponse)
def update_order(
    id: int,
    order_update: schemas.OrderUpdate,
    db=Depends(get_db)
):
    order = orders_service.update_order(db, id, order_update)

    if order is None:
        raise HTTPException(status_code=404, detail="Objednávka nebola nájdená")

    return order