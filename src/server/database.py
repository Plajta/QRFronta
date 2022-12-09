"""
Bruh this is kinda simple lol, why not

"""

import redis
import uuid


class redisbase:
    def __init__(self, redis_host="localhost", redis_port=6379, redis_password=""):
        self.Redis = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    def add(self, useruuid, username):
        try:
            people = self.retrieve_raw() or ""
            people = people+str(useruuid)+","+username+";"
            self.set(people)
        except Exception as E:
            print(E)

    def set(self, people:list):
        try:
            write = ""
            for peep in people:
                write = write + str(peep) + ";"
            write = write[:-1]
            self.set(write)
        except Exception as E:
            print(E)

    def set(self, people:str):
        try:
            self.Redis.set("people", people)
        except Exception as E:
            print(E)

    def retrieve_raw(self):
        try:
            return self.Redis.get("people")
        except Exception as E:
            print(E)

    def retrieve_all(self):
        try:
            peoplelist = self.Redis.get("people")[:-1]
            if peoplelist == None: peoplelist = []
            else: peoplelist = peoplelist.split(";")
            
            people = []
            if len(peoplelist) != 0:
                for peep in peoplelist:
                    # print(uuid.UUID(liduch))
                    people.append(uuid.UUID(peep))
            
            return people
        except Exception as E:
            print(E)

    def delete(self):
        try:
            self.Redis.delete("people")
        except Exception as E:
            print(E)
