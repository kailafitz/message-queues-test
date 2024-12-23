# Message Queue Test (Local)

### Set Up
* python3 -m virtualenv venv
* source venv/bin/activate
* python3 -m pip install pika
* python3 -m pip install rabbitmq
* python3 -m pip install redis
* python3 -m pip install python-dotenv
* pip freeze > requirements.txt
* Install docker image from https://hub.docker.com/_/rabbitmq
* Install redis image from https://hub.docker.com/r/redis/redis-stack

### Run
* python3 producer.py
* python3 consumer.py
* python3 main.py

### Run
* Log into https://customer.cloudamqp.com/instance
* Click into RabbitMQ Manager
* Go to Queues and Streams tab
* Select the name of the service so in this case "test"
