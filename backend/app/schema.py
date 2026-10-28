from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models import AccountType


# request for account
class AccountCreate(BaseModel):
    name: str
    bank_name: str
    account_type: AccountType
    initial_balance: float


# response for account
class AccountRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    bank_name: str
    account_type: AccountType
    initial_balance: float


# request for category
class CategoryCreate(BaseModel):
    name: str


# response for category
class CategoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


# request for recurring expenses
class RecurringExpenseCreate(BaseModel):
    name: str
    category_id: int
    amount: float
    frequency: str
    next_due_date: datetime
    is_active: bool


# response for recurring expenses
class RecurringExpenseRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category_id: int
    name: str
    amount: float
    frequency: str
    next_due_date: datetime
    is_active: bool


# request for transaction
class TransactionCreate(BaseModel):
    source_account_id: int
    destination_account_id: int | None = None
    category_id: int | None = None
    recurring_expense_id: int | None = None
    transaction_type: str
    date: datetime
    description: str | None = None
    amount: float


# response for transaction
class TransactionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    source_account_id: int
    destination_account_id: int | None = None
    recurring_expense_id: int | None = None
    transaction_type: str
    category_id: int | None = None
    date: datetime
    description: str | None = None
    amount: float
