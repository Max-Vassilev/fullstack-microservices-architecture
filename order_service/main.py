from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from order_model import Order
from order_schema import OrderCreate, OrderRead
import requests

app = FastAPI()
USER_SERVICE_URL = "http://localhost:8001"


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/orders", response_model=OrderRead)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    if order.quantity <= 0:
        raise HTTPException(status_code=400, detail="Quantity must be positive")

    response = requests.get(f"{USER_SERVICE_URL}/users/{order.user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid user ID")

    db_order = Order(
        product_name=order.product_name,
        quantity=order.quantity,
        price=order.price,
        user_id=order.user_id,
    )

    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order


@app.get("/orders/{order_id}", response_model=OrderRead)
def get_order(order_id: int, session: Session = Depends(get_session)):
    db_order = session.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
