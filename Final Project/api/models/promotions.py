from sqlalchemy import Column, Integer, String, Boolean, TEXT
from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(50), unique=True, nullable=False)
    description = Column(TEXT, nullable=True)
    discount_percentage = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False, default=True)