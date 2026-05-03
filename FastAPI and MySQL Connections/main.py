from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, ConfigDict
from typing import Annotated, Optional
from sqlalchemy import func
import models
from database import engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(get_db)]

class UserBase(BaseModel):
    name: str
    age: int
    gender: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TodoBase(BaseModel):
    task_body: str
    due_day: int
    due_month: str
    due_year: int
    user_id: int


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    task_body: Optional[str] = None
    due_day: Optional[int] = None
    due_month: Optional[str] = None
    due_year: Optional[int] = None
    user_id: Optional[int] = None


class Todo(TodoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: db_dependency):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/", response_model=list[User], status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency):
    return db.query(models.User).all()
    
@app.post("/todos/", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate, db: db_dependency):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos/", response_model=list[Todo], status_code=status.HTTP_200_OK)
async def get_todos(db: db_dependency):
    return db.query(models.Todo).all()

@app.put("/todos/{todo_id}", response_model=Todo, status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int, todo_request: TodoUpdate, db: db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id)
    if db_todo.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    
    update_data = todo_request.model_dump(exclude_unset=True)
    db_todo.update(update_data, synchronize_session=False)
    db.commit()
    
    return db_todo.first()

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, db: db_dependency):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id)
    if db_todo.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    
    db_todo.delete(synchronize_session=False)
    db.commit()
    
    return None


@app.get("/users_count/", status_code=status.HTTP_200_OK)
async def get_users_count(db: db_dependency):
    count_result = db.query(func.count(models.User.id)).scalar()
    return {"user_count": count_result}


@app.get("/user_todo_by_month/", response_model=list[Todo], status_code=status.HTTP_200_OK)
async def get_user_todo_by_month(user_name: str, month: str, db: db_dependency):
    return (
        db.query(models.Todo)
        .join(models.User)
        .filter(models.User.name == user_name, models.Todo.due_month == month)
        .all()
    )


@app.get("/user_by_todo/", status_code=status.HTTP_200_OK)
async def get_user_by_todo(todo: str, db: db_dependency):
    db_users = (
        db.query(models.User.id, models.User.name, models.User.age, models.User.gender)
        .join(models.Todo)
        .filter(models.Todo.task_body.like(f"%{todo}%"))
        .all()
    )

    return [
        {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "gender": user.gender,
        }
        for user in db_users
    ]