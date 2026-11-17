from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Account, Category, RecurringExpense, Transaction
from app.schema import TransactionCreate, TransactionRead
from app.session import get_db

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.post("", response_model=TransactionRead)
def create_transaction(payload: TransactionCreate, db: Session = Depends(get_db)):
    # source account part
    source_account = db.get(Account, payload.source_account_id)
    if not source_account:
        raise HTTPException(status_code=400, detail="Source Account doesn't exist")

    # destination account part - internal money movements basically
    if payload.destination_account_id is not None:
        destination_account = db.get(Account, payload.destination_account_id)
        if not destination_account:
            raise HTTPException(
                status_code=400, detail="Destination Account doesn't exist"
            )

    # category bit
    if payload.category_id is not None:
        category_id_received = db.get(Category, payload.category_id)
        if not category_id_received:
            raise HTTPException(status_code=400, detail="Invalid category ID")

    # recurring expenses
    if payload.recurring_expense_id is not None:
        received_recurring = db.get(RecurringExpense, payload.recurring_expense_id)
        if not received_recurring:
            raise HTTPException(status_code=400, detail="Invalid Recurring Expense ID")

    new_transaction = Transaction(**payload.model_dump())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction


@router.get("", response_model=list[TransactionRead])
def read_transactions(db: Session = Depends(get_db)):
    fetchall_transactions = db.query(Transaction).all()
    return fetchall_transactions


@router.get("/{transaction_id}", response_model=TransactionRead)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    fetched_transaction = db.get(Transaction, transaction_id)
    if not fetched_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return fetched_transaction
