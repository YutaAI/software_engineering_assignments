from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..dependencies.database import get_db

router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("/", response_model=schema.CustomerOut)
def create(request: schema.CustomerCreate, db: Session = Depends(get_db)):
	return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.CustomerOut])
def read_all(db: Session = Depends(get_db)):
	return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.CustomerOut)
def read_one(item_id: int, db: Session = Depends(get_db)):
	return controller.read_one(db, item_id=item_id)

