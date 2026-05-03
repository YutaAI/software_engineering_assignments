from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..dependencies.database import get_db
from ..models.orders import Order

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    total_orders = db.query(Order).count()
    totals_by_status = (
        db.query(Order.order_status, func.count(Order.id))
        .group_by(Order.order_status)
        .all()
    )
    return {"total_orders": total_orders, "by_status": dict(totals_by_status)}


@router.get("/orders_by_status")
def orders_by_status(db: Session = Depends(get_db)):
    rows = db.query(Order.order_status, func.count(Order.id)).group_by(Order.order_status).all()
    return {r[0]: r[1] for r in rows}
