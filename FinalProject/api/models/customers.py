from sqlalchemy import Column, String, Integer
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    email = Column(String(200), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(String(300), nullable=True)
