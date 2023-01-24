import hashlib

from sqlalchemy.orm import Session
from ..adapters.database import db, Base
from ..models.package_event import Event, OutboxEvent

def recreate_database():
    """
        Recreate database tables
    """    
    Base.metadata.drop_all(db) 
    Base.metadata.create_all(db)

def record_event(*args, **kwargs) -> Event:
    """
        Commit both data in the same transaction
    """
    print(str(kwargs))
    with Session(db) as session:        
        h = hashlib.new('sha256')
        h.update(str(kwargs).encode())
        uuid = h.hexdigest()
        print(uuid, len(uuid))
        evt = Event(id = uuid, *args, **kwargs)
        session.add(evt)
        outbox_evt = OutboxEvent(id = uuid, *args, **kwargs)
        session.add(outbox_evt)
        session.commit()
        return evt
    return None