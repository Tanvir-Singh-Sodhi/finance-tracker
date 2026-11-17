from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Account
from app.schema import AccountCreate, AccountRead
from app.session import get_db

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("", response_model=AccountRead)
def create_account(payload: AccountCreate, db: Session = Depends(get_db)):
    new_account = Account(**payload.model_dump())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account


@router.get("", response_model=list[AccountRead])
def read_accounts(db: Session = Depends(get_db)):
    fetched_accounts = db.query(Account).all()
    return fetched_accounts


@router.get("/{account_id}", response_model=AccountRead)
def read_account(account_id: int, db: Session = Depends(get_db)):
    fetched_account = db.get(Account, account_id)
    if not fetched_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return fetched_account
