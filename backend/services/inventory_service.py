import models


def get_all_inventory_items(db):
    return db.query(models.InventoryItem).all()

def get_inventory_item_by_id(db, item_id: int):
    return (
        db.query(models.InventoryItem)
        .filter(models.InventoryItem.id == item_id)
        .first()
    )

def create_inventory_item(db, item):
    new_item = models.InventoryItem(
        item_name=item.item_name,
        item_type=item.item_type,
        current_quantity=item.current_quantity,
        minimum_quantity=item.minimum_quantity,
        unit=item.unit
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

def update_inventory_item(db, item_id: int, item_update):
    item = get_inventory_item_by_id(db, item_id)

    if item is None:
        return None

    if item_update.current_quantity is not None:
        item.current_quantity = item_update.current_quantity

    if item_update.minimum_quantity is not None:
        item.minimum_quantity = item_update.minimum_quantity

    if item_update.status is not None:
        item.status = item_update.status

    db.commit()
    db.refresh(item)

    return item