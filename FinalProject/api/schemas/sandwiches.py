from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float
    calories: Optional[int] = None
    food_category: Optional[str] = None


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None


class Sandwich(SandwichBase):
    id: int
    model_config = ConfigDict(from_attributes=True)