import os
import pika
from dotenv import load_dotenv

load_dotenv()

# Step 1: Establish a connection with RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(os.environ.get("RABBITMQ_CONNECTION_STRING")))
channel = connection.channel()

# Step 2: Create a queue named "hello_queue"
channel.queue_declare(queue=os.environ.get("SERVICE_NAME"), durable=True)

# Step 3: Send a message to the queue
message = "Hello, RabbitMQ!"
channel.basic_publish(exchange="", routing_key=os.environ.get("SERVICE_NAME"), body=message)

print(f" [x] Sent '{message}'")

# Step 4: Close the connection
connection.close()
