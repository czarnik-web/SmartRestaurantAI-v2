from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey , func
from database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=True)
    order_number = Column(String, nullable=False, unique=True)
    order_date = Column(DateTime, server_default=func.now())
    order_type = Column(String, nullable=False)
    order_status = Column(String, nullable=False, default="New")
    total_amount = Column(Float, nullable=False, default=0.0)
    payment_status = Column(String, nullable=False, default="Pending")
    items = relationship(
    "OrderItem",
    back_populates="order",
    cascade="all, delete-orphan"
)

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    order = relationship(
    "Order",
    back_populates="items"
)

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False, unique=True)
    payment_method = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="Pending")
    payment_date = Column(DateTime, server_default=func.now())

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    item_type = Column(String, nullable=False)
    current_quantity = Column(Float, nullable=False, default=0.0)
    minimum_quantity = Column(Float, nullable=False, default=0.0)
    unit = Column(String, nullable=False)
    status = Column(String, nullable=False, default="Active")

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=True)
    type = Column(String, nullable=False)
    message = Column(String, nullable=False)
    status = Column(String, nullable=False, default="Pending")