import uuid

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Index

from sqlalchemy.orm import relationship

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy_json import mutable_json_type

from ..adapters.database import Base

from datetime import datetime

PackageEventMetaData = Base.metadata

# Event model 
class Event(Base):
    __tablename__ = "event"

    id = Column(String(64), primary_key=True)
    package_id = Column(Integer, nullable=False)
    type = Column(String)
    attributes = Column(mutable_json_type(dbtype=JSONB, nested=True))
    created_at = Column(DateTime, default=datetime.utcnow)

    # __table_args__ = (
    #     Index('evt_package_id_index', package_id, created_at.asc()),
    # )

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        return "<PackageEvent(id='%s', package_id='%s', type='%s', attributes='%s')>" % (
            self.id,
            self.package_id,
            self.type,
            self.attributes
        )


# Outbox model (exact copy)
class OutboxEvent(Base):
    __tablename__ = "outbox_event"    

    id = Column(String(64), primary_key=True)
    package_id = Column(Integer, nullable=False)
    type = Column(String)
    attributes = Column(mutable_json_type(dbtype=JSONB, nested=True))
    created_at = Column(DateTime, default=datetime.utcnow)

    # __table_args__ = (
    #     Index('out_package_id_index', package_id, created_at.asc()),
    # )
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def __repr__(self):
        return "<PackageEvent(id='%s', package_id='%s', type='%s', attributes='%s')>" % (
            self.id,
            self.package_id,
            self.type,
            self.attributes
        )

