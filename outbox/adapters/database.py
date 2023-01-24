from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db_source = "postgresql://postgres:example@localhost:5432/postgres"

db = create_engine(db_source)

Base = declarative_base()
