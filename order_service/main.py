from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Product, Order, ItemAndCountInBasket
from order_service.schemas import (
    ProductCreate, ProductRead,
    OrderCreate, OrderRead,
    ItemAndCountInBasketRead
)

import requests

app = FastAPI()
USER_SERVICE_URL = "http://localhost:8001"

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products", response_model=ProductRead)
def create_product(product: ProductCreate, session: Session = Depends(get_session)):
    db_product = Product(name=product.name, description=product.description, price=product.price)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@app.get("/products/{product_id}", response_model=ProductRead)
def get_product(product_id: int, session: Session = Depends(get_session)):
    db_product = session.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.post("/orders", response_model=OrderRead)
def create_order(order: OrderCreate, session: Session = Depends(get_session)):
    response = requests.get(f"{USER_SERVICE_URL}/users/{order.user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    db_order = Order(product_name=order.product_name, quantity=order.quantity, price=order.price, user_id=order.user_id)
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

@app.get("/item_and_count_in_basket/{order_id}", response_model=List[ItemAndCountInBasketRead])
def get_items_in_basket(order_id: int, session: Session = Depends(get_session)):
    items = session.query(ItemAndCountInBasket).filter(ItemAndCountInBasket.order_id == order_id).all()
    return items
