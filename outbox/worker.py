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

POOLING_INTERVAL = 10
AGGREGATOR_KEY = 'package_id'
MAX_EVENTS = 3

print(text2art("Worker"))
logging.info("Outbox worker is starting...")
logging.info(f"Pooling by agg key package_id")
logging.info(f"MAX_EVENTS = {MAX_EVENTS}, POOLING_INTERVAL = {POOLING_INTERVAL}")
logging.info("")
while True:
    with Session(db) as session:       
        # busca os eventos do pacote
        eventos = session.execute(select(OutboxEvent)
            .order_by(OutboxEvent.created_at)
            .limit(MAX_EVENTS)
            .with_for_update(read = True, nowait = True))
        num_eventos = 0
        for evento in eventos:
            print("type: ", type(evento))
            # Processar evento e remover
            print("Processando evento ", evento[0].as_dict())
            send_message(evento[0].as_dict())
            session.delete(evento[0])
            num_eventos += 1
        # Commit
        session.commit()
        if num_eventos > 1:
            logging.info(f'Events processed: {num_eventos}.')
            logging.info('---')
    logging.debug('Waiting pooling interval...')
    time.sleep(POOLING_INTERVAL)