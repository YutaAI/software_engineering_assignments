from typing import Optional
from pydantic import BaseModel


class FeedbackBase(BaseModel):
    customer_name: str
    rating: int
    comment: Optional[str] = None
    order_id: Optional[int] = None


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(BaseModel):
    customer_name: Optional[str] = None
    rating: Optional[int] = None
    comment: Optional[str] = None
    order_id: Optional[int] = None


class Feedback(FeedbackBase):
    id: int

    class ConfigDict:
        from_attributes = True