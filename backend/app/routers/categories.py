from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Category
from app.schema import CategoryCreate, CategoryRead
from app.session import get_db

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("", response_model=CategoryRead)
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**payload.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.get("", response_model=list[CategoryRead])
def read_categories(db: Session = Depends(get_db)):
    fetchall_categories = db.query(Category).all()
    return fetchall_categories


@router.get("/{category_id}", response_model=CategoryRead)
def read_category(category_id: int, db: Session = Depends(get_db)):
    fetched_category = db.get(Category, category_id)
    if not fetched_category:
        raise HTTPException(status_code=404, detail="Category does not exist")
    return fetched_category
