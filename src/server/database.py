"""
Bruh this is kinda simple lol, why not

"""

import redis
import uuid

redis_host = "localhost"

redis_port = 6379
redis_password = ""

# The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
# using the default encoding utf-8.  This is client specific.
Redis = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

def Redis_Set(lidi):
    try:
        zapis = ""
        for liduch in lidi:
            zapis = zapis+str(liduch)+";"
        zapis = zapis[:-1]
        Redis.set("people", zapis)
    except Exception as E:
        print(E)

def Redis_Retrieve():
    try:
        listlidi = Redis.get("people").split(";")
        lidi = []
        for liduch in listlidi:
            #print(uuid.UUID(liduch))
            lidi.append(uuid.UUID(liduch))
        return lidi
    except Exception as E:
        print(E)

def Redis_delete():
    try:
        Redis.delete("people")
    except Exception as E:
        print(E)