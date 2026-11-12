from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.models import Account, Category
from app.schema import AccountCreate, AccountRead, CategoryCreate, CategoryRead
from app.session import get_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "ok"}


@app.post("/accounts", response_model=AccountRead)
def create_account(payload: AccountCreate, db: Session = Depends(get_db)):
    new_account = Account(**payload.model_dump())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account


@app.get("/accounts", response_model=list[AccountRead])
def read_accounts(db: Session = Depends(get_db)):
    fetched_accounts = db.query(Account).all()
    return fetched_accounts


@app.get("/accounts/{account_id}", response_model=AccountRead)
def read_account(account_id: int, db: Session = Depends(get_db)):
    fetched_account = db.get(Account, account_id)
    if not fetched_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return fetched_account


@app.post("/categories", response_model=CategoryRead)
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Category(**payload.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@app.get("/categories", response_model=list[CategoryRead])
def read_categories(db: Session = Depends(get_db)):
    fetchall_categories = db.query(Category).all()
    return fetchall_categories


@app.get("/categories/{category_id}", response_model=CategoryRead)
def read_category(category_id: int, db: Session = Depends(get_db)):
    fetched_category = db.get(Category, category_id)
    if not fetched_category:
        raise HTTPException(status_code=404, detail="Category does not exist")
    return fetched_category
