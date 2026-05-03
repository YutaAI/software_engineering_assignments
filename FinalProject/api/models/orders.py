from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    customer_phone = Column(String(50), nullable=True)
    delivery_address = Column(String(300), nullable=True)
    order_type = Column(String(50), nullable=True)
    payment_method = Column(String(50), nullable=True)
    order_status = Column(String(50), nullable=True)
    tracking_number = Column(String(100), nullable=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    order_details = relationship("OrderDetail", back_populates="order")