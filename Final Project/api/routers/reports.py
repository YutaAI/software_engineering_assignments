from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import reports as controller
from ..dependencies.database import get_db


router = APIRouter(
    tags=['Reports'],
    prefix="/reports"
)


@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    return controller.summary(db)


@router.get("/orders-by-status")
def orders_by_status(db: Session = Depends(get_db)):
    return controller.orders_by_status(db)