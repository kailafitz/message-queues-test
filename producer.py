import pika

# Step 1: Establish a connection with RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters('amqps://zdtavylq:BOsStEV5XSccxnba9s-Ik3g0rYi1zT_F@vulture.rmq.cloudamqp.com/zdtavylq'))
channel = connection.channel()

# Step 2: Create a queue named 'hello_queue'
channel.queue_declare(queue='test', durable=True)

# Step 3: Send a message to the queue
message = "Hello, RabbitMQ!"
channel.basic_publish(exchange='', routing_key='test', body=message)

print(f" [x] Sent '{message}'")

# Step 4: Close the connection
connection.close()
