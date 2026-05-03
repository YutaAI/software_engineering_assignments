from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict


class PromotionBase(BaseModel):
    promo_code: str
    description: Optional[str] = None
    discount_percentage: int
    active: Optional[bool] = True


class PromotionCreate(PromotionBase):
    pass


class PromotionOut(PromotionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
