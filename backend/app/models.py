# this is where i expect to make the final ERD to sqlA conversion
# going to work on 'Account' table

import enum

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base

# using sqlite to create a local db file
db_url = "sqlite:///./finance.db"

engine = create_engine(db_url)
base = declarative_base()


# now we can actually make a table called 'Account'
class AccountType(enum.Enum):
    CURRENT = "current"
    SAVINGS = "savings"


class Account(base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bank_name = Column(String, nullable=False)
    account_type = Column(Enum(AccountType), nullable=False)
    initial_balance = Column(Numeric, nullable=False)


class Category(base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class RecurringExpense(base):
    __tablename__ = "recurring_expenses"
    id = Column(Integer, primary_key=True)
    category_id = Column(ForeignKey("categories.id"), nullable=False)
    name = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    frequency = Column(String, nullable=False)
    next_due_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)


class Transaction(base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    source_account_id = Column(ForeignKey("accounts.id"), nullable=False)
    destination_account_id = Column(ForeignKey("accounts.id"))
    category_id = Column(ForeignKey("categories.id"))
    recurring_expense_id = Column(ForeignKey("recurring_expenses.id"))
    transaction_type = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String)
    amount = Column(Numeric, nullable=False)


base.metadata.create_all(engine)
