"""
Bruh this is kinda simple lol, why not

"""

import redis

redis_host = "localhost"

redis_port = 6379
redis_password = ""

# The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
# using the default encoding utf-8.  This is client specific.
Redis = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

def Redis_Add(num):
    try:
        Redis.set("count", num)
    except Exception as E:
        print(E)

def Redis_Retrieve():
    try:
        count = Redis.get("count")
        return count      

    except Exception as E:
        print(E)

def Redis_delete():
    try:
        Redis.delete("count")
    except Exception as E:
        print(E)