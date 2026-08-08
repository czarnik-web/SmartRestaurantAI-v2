import models


def get_all_products(db):
    return db.query(models.Product).all()
def get_product_by_id(db, product_id: int):
    return (
        db.query(models.Product)
        .filter(models.Product.id == product_id)
        .first()
    )

def create_product(db, product):
    new_product = models.Product(
        name=product.name,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def update_product(db, product_id: int, product_update):
    product = get_product_by_id(db, product_id)

    if product is None:
        return None

    if product_update.name is not None:
        product.name = product_update.name

    if product_update.price is not None:
        product.price = product_update.price

    db.commit()
    db.refresh(product)

    return product