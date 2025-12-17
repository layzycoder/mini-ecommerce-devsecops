from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItem(BaseModel):
    product_id: str
    name: str
    price: float
    quantity: int

class Order(BaseModel):
    id: str | None = None
    items: List[OrderItem]
    total_amount: float
    currency: str = "USD"
    status: str = "CREATED"
    created_at: datetime | None = None
