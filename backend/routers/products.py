from fastapi import APIRouter, HTTPException, Depends
import schemas
from database import SessionLocal
from services import products_service

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{id}", response_model=schemas.ProductResponse)
def get_product(id: int, db = Depends(get_db)):
    product = products_service.get_product_by_id(db, id)

    if product is None:
        raise HTTPException(status_code=404, detail="Produkt nebol nájdený")

    return product

@router.get("", response_model=list[schemas.ProductResponse])
def get_products(db = Depends(get_db)):
    return products_service.get_all_products(db)

@router.post("", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db = Depends(get_db)):
    return products_service.create_product(db, product)

@router.patch("/{id}", response_model=schemas.ProductResponse)
def update_product(
    id: int,
    product_update: schemas.ProductUpdate,
    db=Depends(get_db)
):
    product = products_service.update_product(db, id, product_update)

    if product is None:
        raise HTTPException(status_code=404, detail="Produkt nebol nájdený")

    return product