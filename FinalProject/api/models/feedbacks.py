from sqlalchemy import Column, ForeignKey, Integer, String, TEXT
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    customer_name = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(TEXT, nullable=True)

    order = relationship("Order")
