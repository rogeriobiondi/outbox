import os
import time
import json
import boto3

from botocore.config import Config

from ..util.encoders import DateTimeEncoder

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY_ID = os.getenv('AWS_SECRET_KEY_ID')
AWS_ENDPOINT_URL  = os.getenv('AWS_ENDPOINT_URL')
SQS_QUEUE_URL  = os.getenv('SQS_QUEUE_URL')
SQS_POOLING_INTERVAL = int(os.getenv('SQS_POOLING_INTERVAL'))

config = Config(
    region_name = 'us-east-1',    
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

client = boto3.client(service_name = 'sqs',
     endpoint_url = AWS_ENDPOINT_URL,
     aws_access_key_id = AWS_ACCESS_KEY_ID,
     aws_secret_access_key = AWS_SECRET_KEY_ID,
     config = config
)


def send_message(message: dict) -> dict:
    """
        Send SQS Message
    """
    response = client.send_message(
        QueueUrl = f'{SQS_QUEUE_URL}', 
        MessageBody = json.dumps(message, indent = 2, cls = DateTimeEncoder)
    )
    return(response)

def receive_messages() -> dict:
    while True:
        response = client.receive_message(QueueUrl = f'{SQS_QUEUE_URL}')
        if 'Messages' in response:
            # Read messages
            for message in response['Messages']:
                print(message['Body'])
                # do whateaver you like with the message
                # ...
                # Remove message from queue
                client.delete_message(QueueUrl = f'{SQS_QUEUE_URL}', ReceiptHandle = message['ReceiptHandle'])
        time.sleep(SQS_POOLING_INTERVAL/1000)