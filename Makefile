# include .env
# export $(shell sed 's/=.*//' .env)
# export PYTHONPATH=$(CURDIR)/src


install:
	@echo "creating the environment..."
	# @pyenv install 3.10.4
	@pyenv virtualenv 3.10.4 outbox_python
	@pyenv local outbox_python
	@echo "installing Poetry..."
	@curl -sSL https://install.python-poetry.org | python3 -
	@pip install localstack
	@pip install awscli-local
	@pip install alembic
	@poetry install
	@echo "OK"

clear:
	@printf "cleaning temp files... "
	@rm -f dist/*.gz
	@rm -rfd *.egg-info
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete
	@find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
	@echo "OK"

infra-start:
	@docker-compose up -d
	
infra-create:
	@alembic revision --autogenerate -m "First commit"
	@alembic upgrade heads
	@awslocal sqs create-queue --queue-name packtrack-events

infra-stop:
	@docker-compose down

populate: 
	@python -B -m outbox.populate

worker: 
	@python -B -m outbox.worker

receiver: 
	@python -B -m outbox.receiver