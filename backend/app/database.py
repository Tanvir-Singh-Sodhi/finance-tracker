from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///./finance.db"
engine = create_engine(db_url)
base = declarative_base()
