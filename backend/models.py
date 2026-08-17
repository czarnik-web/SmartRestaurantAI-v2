from sqlalchemy import Column, Integer, String, Float, DateTime, func
from database import Base


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