from sqlalchemy import Column, String, Integer, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    payment_method = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # order_id is a reference to the order for which the payment was made.
    # we don't use a real foreign key because each microservice
    # has its own PostgreSQL instance and database, so tables
    # from different services cannot be linked directly.
    order_id = Column(Integer, nullable=False)
