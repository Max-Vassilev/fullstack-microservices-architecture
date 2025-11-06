from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from uuid import uuid4

app = FastAPI()
payments = {}

ORDER_SERVICE_URL = "http://localhost:8002"


class Payment(BaseModel):
    order_id: str
    amount: float


@app.post("/payments")
def make_payment(payment: Payment):
    # validate order
    response = requests.get(f"{ORDER_SERVICE_URL}/orders/{payment.order_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid order ID")

    payment_id = str(uuid4())
    payments[payment_id] = payment
    return {"id": payment_id, "payment": payment}


@app.get("/payments/{payment_id}")
def get_payment(payment_id: str):
    payment = payments.get(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
