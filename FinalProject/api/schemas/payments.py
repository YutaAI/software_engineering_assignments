from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict


class PaymentBase(BaseModel):
    order_id: int
    amount: float
    method: str
    status: Optional[str] = "pending"


class PaymentCreate(PaymentBase):
    pass


class PaymentOut(PaymentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
