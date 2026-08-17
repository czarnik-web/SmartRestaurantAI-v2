from fastapi import APIRouter, HTTPException, Depends

import schemas

from database import SessionLocal
from services import kitchen_service


router = APIRouter(
    prefix="/kitchen/orders",
    tags=["Kitchen"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[schemas.OrderResponse])
def get_kitchen_orders(db=Depends(get_db)):
    return kitchen_service.get_all_kitchen_orders(db)

@router.get("/{id}", response_model=schemas.OrderResponse)
def get_kitchen_order(id: int, db=Depends(get_db)):
    order = kitchen_service.get_kitchen_order_by_id(db, id)

    if order is None:
        raise HTTPException(status_code=404, detail="Objednávka nebola nájdená")

    return order

@router.patch("/{id}/status", response_model=schemas.OrderResponse)
def update_kitchen_order_status(
    id: int,
    status: str,
    db=Depends(get_db)
):
    order = kitchen_service.update_kitchen_order_status(db, id, status)

    if order is None:
        raise HTTPException(status_code=404, detail="Objednávka nebola nájdená")

    return order