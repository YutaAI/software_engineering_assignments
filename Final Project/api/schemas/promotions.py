from typing import Optional
from pydantic import BaseModel


class PromotionBase(BaseModel):
    promo_code: str
    description: Optional[str] = None
    discount_percentage: int
    active: Optional[bool] = True


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    promo_code: Optional[str] = None
    description: Optional[str] = None
    discount_percentage: Optional[int] = None
    active: Optional[bool] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True