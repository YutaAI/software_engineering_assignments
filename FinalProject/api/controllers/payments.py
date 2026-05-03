from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.payments import Payment
from ..schemas.payments import PaymentCreate, PaymentOut

router = APIRouter(prefix="/payments", tags=["payments"])


@router.post("/", response_model=PaymentOut)
def create_payment(payload: PaymentCreate, db: Session = Depends(get_db)):
    pay = Payment(**payload.model_dump())
    db.add(pay)
    db.commit()
    db.refresh(pay)
    return pay


@router.get("/", response_model=list[PaymentOut])
def list_payments(db: Session = Depends(get_db)):
    return db.query(Payment).all()
