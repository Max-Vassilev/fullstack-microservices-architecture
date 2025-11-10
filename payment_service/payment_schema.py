from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: str
    amount: float

class PaymentResponse(PaymentBase):
    id: int
