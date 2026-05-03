from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict


class FeedbackBase(BaseModel):
    order_id: Optional[int] = None
    customer_name: str
    rating: int
    comment: Optional[str] = None


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackOut(FeedbackBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
