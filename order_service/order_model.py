from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    
    # user_id is a reference to the user who created the order.
    # we don't use a real foreign key because each microservice
    # has its own PostgreSQL instance and database, so tables
    # from different services cannot be linked directly.
    user_id = Column(Integer, nullable=False)
