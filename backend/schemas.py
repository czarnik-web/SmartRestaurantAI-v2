from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    model_config = {
        "from_attributes": True
    }
class OrderCreate(BaseModel):
    customer_id: int | None = None
    order_number: str
    order_type: str
    total_amount: float


class OrderUpdate(BaseModel):
    order_status: str | None = None
    payment_status: str | None = None


class OrderResponse(BaseModel):
    id: int
    customer_id: int | None
    order_number: str
    order_type: str
    order_status: str
    total_amount: float
    payment_status: str

    model_config = {
        "from_attributes": True
    }

class PaymentCreate(BaseModel):
    order_id: int
    payment_method: str
    amount: float


class PaymentUpdate(BaseModel):
    status: str | None = None


class PaymentResponse(BaseModel):
    id: int
    order_id: int
    payment_method: str
    amount: float
    status: str

    model_config = {
        "from_attributes": True
    }