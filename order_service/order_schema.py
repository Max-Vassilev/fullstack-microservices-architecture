from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_name: str
    quantity: int
    price: float
    user_id: int

class OrderRead(OrderCreate):
    id: int

    class Config:
        orm_mode = True
