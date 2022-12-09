"""
Bruh this is kinda simple lol, why not

"""

import redis
import uuid


class RedisBase:
    def __init__(self, redis_host="localhost", redis_port=6379, redis_password=""):
        self.Redis = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    def add(self, useruuid, username):  # For adding people to the end of the queue
        try:
            people = self.retrieve_raw() or ""
            people = people+str(useruuid)+","+username
            self.set(people)
        except Exception as E:
            print(E)

    def set_list(self, people: list):  # For setting the list of people in queue
        try:
            write = ""
            for peep in people:
                write = write + str(peep) + ";"
            self.set(write)
        except Exception as E:
            print(E)

    def set(self, people: str):   # For setting the raw contents
        try:
            if people[-1] != ";":
                people = people+";"
            self.Redis.set("people", people)
        except Exception as E:
            print(E)

    def retrieve_raw(self):  # Retrieves all data in the raw form
        try:
            return self.Redis.get("people")
        except Exception as E:
            print(E)

    def retrieve_all(self):  # Retrieves all data as a list of UUIDs and Names split with a colon
        try:
            people = self.Redis.get("people")[:-1].split(";")
            return people
        except Exception as E:
            print(E)

    def retrieve_uuid(self):  # Retrieves a list of UUIDs (strips them of the names)
        try:
            peoplelist = self.retrieve_all()
            people = []
            for peep in peoplelist:
                people.append(uuid.UUID(peep.split(",")[0]))
            return people
        except Exception as E:
            print(E)

    def retrieve_count(self):  # Retrieves the number of entries in the database (people in the queue)
        return len(self.retrieve_all())

    def delete(self, toremove: str):
        try:
            removed = self.retrieve_all()
            removed.remove(toremove)
            self.set_list(removed)
        except Exception as E:
            print(E)

    def delete(self, index: int):
        try:
            popped = self.retrieve_all()
            popped.pop(index)
            self.set_list(popped)
        except Exception as E:
            print(E)

    def delete_all(self):
        try:
            self.Redis.delete("people")
        except Exception as E:
            print(E)
