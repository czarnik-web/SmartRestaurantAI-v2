from fastapi import APIRouter, HTTPException, Depends

import schemas

from database import SessionLocal
from services import inventory_service


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=list[schemas.InventoryItemResponse])
def get_inventory_items(db=Depends(get_db)):
    return inventory_service.get_all_inventory_items(db)

@router.get("/{id}", response_model=schemas.InventoryItemResponse)
def get_inventory_item(id: int, db=Depends(get_db)):
    item = inventory_service.get_inventory_item_by_id(db, id)

    if item is None:
        raise HTTPException(status_code=404, detail="Skladová položka nebola nájdená")

    return item

@router.post("", response_model=schemas.InventoryItemResponse)
def create_inventory_item(
    item: schemas.InventoryItemCreate,
    db=Depends(get_db)
):
    return inventory_service.create_inventory_item(db, item)

@router.patch("/{id}", response_model=schemas.InventoryItemResponse)
def update_inventory_item(
    id: int,
    item_update: schemas.InventoryItemUpdate,
    db=Depends(get_db)
):
    item = inventory_service.update_inventory_item(db, id, item_update)

    if item is None:
        raise HTTPException(status_code=404, detail="Skladová položka nebola nájdená")

    return item