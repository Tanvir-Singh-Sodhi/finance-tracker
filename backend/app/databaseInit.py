from database import base, engine
from models import Account, Category, RecurringExpense, Transaction  # noqa: F401

print(base.metadata.tables.keys())
base.metadata.create_all(engine)
