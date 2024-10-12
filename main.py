import redis

# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
print(r.execute_command('INFO')['redis_version'])

r.set('foo', 'bar')
# True
val = r.get('foo')

print("val: ", val)
# bar