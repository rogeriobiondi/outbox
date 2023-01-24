import os
import time
import json
import logging

from sqlalchemy.orm import Session
from sqlalchemy import select

from .models.package_event import OutboxEvent
from .adapters.database import db, Base
from .adapters.sqs import send_message

from art import *

logging.basicConfig(level=logging.INFO)

WORKER_POOLING_INTERVAL = int(os.getenv('WORKER_POOLING_INTERVAL'))
WORKER_MAX_EVENTS = int(os.getenv('WORKER_MAX_EVENTS'))

print(text2art("Worker"))

logging.info("Outbox worker is starting...")
logging.info(f"Pooling events...")
logging.info(f"WORKER_MAX_EVENTS = {WORKER_MAX_EVENTS}, WORKER_POOLING_INTERVAL = {WORKER_POOLING_INTERVAL}")
logging.info("")

while True:
    with Session(db) as session:       
        # query events
        events = session.execute(select(OutboxEvent)
            .order_by(OutboxEvent.created_at)
            .limit(WORKER_MAX_EVENTS)
            .with_for_update(read = True, nowait = True))
        num_events = 0
        for event in events:
            # process event and delete
            print("Processing event ", event[0].as_dict())
            send_message(event[0].as_dict())
            session.delete(event[0])
            num_events += 1
        # Commit
        session.commit()
        if num_events > 1:
            logging.info(f'Events processed: {num_events}.')
            logging.info('---')
    logging.debug('Waiting pooling interval...')
    time.sleep(WORKER_POOLING_INTERVAL/1000)