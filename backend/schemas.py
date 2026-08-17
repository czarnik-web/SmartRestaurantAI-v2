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

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    

class OrderCreate(BaseModel):
    customer_id: int | None = None
    order_number: str
    order_type: str
    items: list[OrderItemCreate]


class OrderUpdate(BaseModel):
    order_status: str | None = None
    payment_status: str | None = None

class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float

    model_config = {
        "from_attributes": True
    }


class OrderResponse(BaseModel):
    id: int
    customer_id: int | None
    order_number: str
    order_type: str
    order_status: str
    total_amount: float
    payment_status: str
    items: list[OrderItemResponse]

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

class InventoryItemCreate(BaseModel):
    item_name: str
    item_type: str
    current_quantity: float
    minimum_quantity: float
    unit: str


class InventoryItemUpdate(BaseModel):
    current_quantity: float | None = None
    minimum_quantity: float | None = None
    status: str | None = None


class InventoryItemResponse(BaseModel):
    id: int
    item_name: str
    item_type: str
    current_quantity: float
    minimum_quantity: float
    unit: str
    status: str

    model_config = {
        "from_attributes": True
    }

class NotificationCreate(BaseModel):
    customer_id: int | None = None
    type: str
    message: str


class NotificationResponse(BaseModel):
    id: int
    customer_id: int | None
    type: str
    message: str
    status: str

    model_config = {
        "from_attributes": True
    }

class DailyReportResponse(BaseModel):
    order_count: int
    total_revenue: float
    low_stock_items: list[InventoryItemResponse]

class TopProductResponse(BaseModel):
    product_id: int
    product_name: str
    quantity_sold: int


class SalesReportResponse(BaseModel):
    total_revenue: float
    completed_orders: int
    total_items_sold: int
    top_products: list[TopProductResponse]

class RefundReportResponse(BaseModel):
    refund_count: int
    total_refunded: float