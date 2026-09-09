# this is where i expect to make the final ERD to sqlA conversion
# going to work on 'Account' table

import enum

from sqlalchemy import Column, Enum, Integer, Numeric, String, create_engine
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
    name = Column(String)
    bank_name = Column(String)
    account_type = Column(Enum(AccountType))
    initial_balance = Column(Numeric)


base.metadata.create_all(engine)
