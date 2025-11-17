from pydantic import BaseModel
from typing import List, Optional

# --- Product Schemas ---

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductRead(ProductCreate):
    id: int

    class Config:
        orm_mode = True

# --- ItemAndCountInBasket Schemas ---

class ItemAndCountInBasketRead(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True

# --- Order Schemas ---

class OrderCreate(BaseModel):
    product_name: str
    quantity: int
    price: float
    user_id: int

class OrderRead(OrderCreate):
    id: int
    items: List[ItemAndCountInBasketRead] = []

    class Config:
        orm_mode = True
