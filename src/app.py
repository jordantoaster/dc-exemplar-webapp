import time
import redis
from flask import Flask
import os
import psycopg2

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379) # Standard Redis port, this is why its not defined in the DC file.

def get_hit_count() -> int:
    """
    The basic retry loop lets us attempt our request multiple times if the redis service is not available. 
    This is useful at startup while the application comes online, but also makes our application more resilient 
    if the Redis service needs to be restarted anytime during the app’s lifetime. In a cluster, this also helps 
    handling momentary connection drops between nodes.
    """
    retries: int = 5
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
    count: int = get_hit_count()
    return 'Hello from Docker! I have been seen {} times.\n'.format(count)

@app.route('/db')
def db_data():
    POSTGRES_URI = os.environ['POSTGRES_DATABASE_URI']
    conn = psycopg2.connect(POSTGRES_URI)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM Persons WHERE PersonID = 1""")
    row = cur.fetchone()
    return 'Hello from Docker! I have this {} person.\n'.format(row)