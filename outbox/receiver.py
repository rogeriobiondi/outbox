import logging

from .adapters.sqs import receive_messages
from art import *

logging.basicConfig(level=logging.INFO)

print(text2art("Receiver"))

logging.info(f"Pooling by SQS Queue...")

receive_messages()