from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from uuid import uuid4

app = FastAPI()
orders = {}

USER_SERVICE_URL = "http://localhost:8001"


class Order(BaseModel):
    user_id: str
    item: str
    quantity: int


@app.post("/orders")
def create_order(order: Order):
    # validate user
    response = requests.get(f"{USER_SERVICE_URL}/users/{order.user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid user ID")

    order_id = str(uuid4())
    orders[order_id] = order
    return {"id": order_id, "order": order}


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    order = orders.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
