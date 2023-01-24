from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# from ..models.package_event import PackageEvent, PackageEventOutbox

db_source = "postgresql://postgres:example@localhost:5432/postgres"

db = create_engine(db_source)

Base = declarative_base()
