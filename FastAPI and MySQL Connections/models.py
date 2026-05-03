from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)

    todos = relationship("Todo", back_populates="user")


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task_body = Column(String(500), nullable=False)
    due_day = Column(Integer, nullable=False)
    due_month = Column(String(10), nullable=False)
    due_year = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="todos")
    
