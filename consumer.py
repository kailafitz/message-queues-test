import os
import pika
from dotenv import load_dotenv

load_dotenv()

# Step 1: Establish a connection with RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(os.environ.get("RABBITMQ_CONNECTION_STRING")))
channel = connection.channel()

# Step 2: Create a queue named "hello_queue" (same as in the producer)
channel.queue_declare(queue=os.environ.get("SERVICE_NAME"), durable=True)

# Step 3: Define a callback function to process messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Step 4: Tell RabbitMQ that this consumer will consume messages from "hello_queue"
channel.basic_consume(queue=os.environ.get("SERVICE_NAME"), on_message_callback=callback, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
