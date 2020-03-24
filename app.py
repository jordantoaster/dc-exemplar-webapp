import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    """
    The basic retry loop lets us attempt our request multiple times if the redis service is not available. 
    This is useful at startup while the application comes online, but also makes our application more resilient 
    if the Redis service needs to be restarted anytime during the app’s lifetime. In a cluster, this also helps 
    handling momentary connection drops between nodes.
    """
    retries = 5
    while True:
        try:
            return cache.incr('hits') # Get the value associated with key 'hits' and increment.
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello from Docker! I have been seen {} times.\n'.format(count)