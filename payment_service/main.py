from fastapi import FastAPI, HTTPException
import requests
from payment_schema import PaymentBase, PaymentResponse

app = FastAPI()
payments = {}
payment_counter = 0

ORDER_SERVICE_URL = "http://localhost:8002"

@app.post("/payments", response_model=PaymentResponse)
def make_payment(payment: PaymentBase):
    global payment_counter
    response = requests.get(f"{ORDER_SERVICE_URL}/orders/{payment.order_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid order ID")

    payment_counter += 1
    payments[payment_counter] = payment
    return PaymentResponse(id=payment_counter, **payment.dict())

@app.get("/payments/{payment_id}", response_model=PaymentResponse)
def get_payment(payment_id: int):
    payment = payments.get(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return PaymentResponse(id=payment_id, **payment.dict())
