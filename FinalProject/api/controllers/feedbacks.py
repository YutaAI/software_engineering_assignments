from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.feedbacks import Feedback
from ..schemas.feedbacks import FeedbackCreate, FeedbackOut

router = APIRouter(prefix="/feedbacks", tags=["feedbacks"])


@router.post("/", response_model=FeedbackOut)
def create_feedback(payload: FeedbackCreate, db: Session = Depends(get_db)):
    fb = Feedback(**payload.model_dump())
    db.add(fb)
    db.commit()
    db.refresh(fb)
    return fb


@router.get("/", response_model=list[FeedbackOut])
def list_feedbacks(db: Session = Depends(get_db)):
    return db.query(Feedback).all()
