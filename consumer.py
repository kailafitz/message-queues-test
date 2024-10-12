import pika

# Step 1: Establish a connection with RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters('amqps://zdtavylq:BOsStEV5XSccxnba9s-Ik3g0rYi1zT_F@vulture.rmq.cloudamqp.com/zdtavylq'))
channel = connection.channel()

# Step 2: Create a queue named 'hello_queue' (same as in the producer)
channel.queue_declare(queue='test', durable=True)

# Step 3: Define a callback function to process messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Step 4: Tell RabbitMQ that this consumer will consume messages from 'hello_queue'
channel.basic_consume(queue='test', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
