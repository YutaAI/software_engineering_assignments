from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy import func
from ..models import orders as order_model
from ..models import order_details as order_detail_model
from ..models import sandwiches as sandwich_model
from ..models import feedbacks as feedback_model
from ..models import promotions as promotion_model


def summary(db: Session):
    total_orders = db.query(func.count(order_model.Order.id)).scalar() or 0
    total_feedback = db.query(func.count(feedback_model.Feedback.id)).scalar() or 0
    average_rating = db.query(func.avg(feedback_model.Feedback.rating)).scalar() or 0
    active_promotions = db.query(func.count(promotion_model.Promotion.id)).filter(promotion_model.Promotion.active == True).scalar() or 0

    sold_items = (
        db.query(
            sandwich_model.Sandwich.sandwich_name,
            func.sum(order_detail_model.OrderDetail.amount).label("quantity_sold")
        )
        .join(order_detail_model.OrderDetail, order_detail_model.OrderDetail.sandwich_id == sandwich_model.Sandwich.id)
        .group_by(sandwich_model.Sandwich.sandwich_name)
        .all()
    )

    return {
        "total_orders": total_orders,
        "total_feedback": total_feedback,
        "average_rating": float(average_rating) if average_rating else 0,
        "active_promotions": active_promotions,
        "popular_sandwiches": [
            {"sandwich_name": name, "quantity_sold": int(quantity or 0)}
            for name, quantity in sold_items
        ],
    }


def orders_by_status(db: Session):
    rows = db.query(order_model.Order.order_status, func.count(order_model.Order.id)).group_by(order_model.Order.order_status).all()
    return [{"order_status": status, "count": int(count or 0)} for status, count in rows]