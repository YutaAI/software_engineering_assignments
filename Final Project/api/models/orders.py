from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    customer_phone = Column(String(20), nullable=True)
    delivery_address = Column(String(255), nullable=True)
    order_type = Column(String(20), nullable=True)
    payment_method = Column(String(30), nullable=True)
    order_status = Column(String(30), nullable=False, server_default="received")
    tracking_number = Column(String(32), unique=True, nullable=False)
    order_date = Column(DATETIME, nullable=False, server_default=func.now())
    description = Column(String(300))

    order_details = relationship("OrderDetail", back_populates="order")