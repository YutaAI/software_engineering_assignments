from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict


class CustomerBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerOut(CustomerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
