from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_name: str
    customer_phone: Optional[str] = None
    delivery_address: Optional[str] = None
    order_type: Optional[str] = None
    payment_method: Optional[str] = None
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    delivery_address: Optional[str] = None
    order_type: Optional[str] = None
    payment_method: Optional[str] = None
    order_status: Optional[str] = None
    tracking_number: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_status: Optional[str] = None
    tracking_number: Optional[str] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
