from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.promotions import Promotion
from ..schemas.promotions import PromotionCreate, PromotionOut

router = APIRouter(prefix="/promotions", tags=["promotions"])


@router.post("/", response_model=PromotionOut)
def create_promotion(payload: PromotionCreate, db: Session = Depends(get_db)):
    promo = Promotion(**payload.model_dump())
    db.add(promo)
    db.commit()
    db.refresh(promo)
    return promo


@router.get("/", response_model=list[PromotionOut])
def list_promotions(db: Session = Depends(get_db)):
    return db.query(Promotion).all()
