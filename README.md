# outbox
Sample Python implementation of Outbox Pattern

![outbox design](images/outbox.png)

## Pre-Reqs

- Ubuntu Operating System
- GNU Make
- Poetry (https://github.com/python-poetry/install.python-poetry.org)
- AWS cli


## Set-up

```
# Take a look at Makefile before running
make install
```

## Starting Dabase and LocalStack

```
docker-compose up -d
```

Login adminer:

http://localhost:8080
user: `postgres`
database: `postgres`
password: `example`


## Configure SQS queue (fake queue)


Configure aws cli for fake environment (Localstack)

```
aws configure --profile teste
AWS Access Key ID [None]: fakeAccessKeyId
AWS Secret Access Key [None]: fakeSecretAccessKey
Default region name [None]: us-east-1
Default output format [None]: json
```

Create the fake queue

```
awslocal sqs create-queue --queue-name packtrack-events
{
    "QueueUrl": "http://localhost:4566/000000000000/packtrack-events"
}
```


## Starting

```
cd outbox
poetry init
```


