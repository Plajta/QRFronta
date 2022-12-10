"""
Bruh this is kinda simple lol, why not

"""

import redis
import uuid
from misc import *


class RedisBase:
    def __init__(self, redis_host="localhost", redis_port=6379, redis_password=""):
        self.Redis = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    def add(self, useruuid, username):  # For adding people to the end of the queue
        try:
            people = self.retrieve_raw() or ""
            people = people + str(useruuid) + "," + username
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

    def set(self, people: str):  # For setting the raw contents
        try:
            if people[-1] != ";":
                people = people + ";"
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
            people_db = self.Redis.get("people")
            if people_db is None:
                people = []
            else:
                people = people_db[:-1].split(";")
            return people

        except Exception as E:
            print(E)

    def retrieve_uuid(self):  # Retrieves a list of UUIDs (strips them of the names)
        try:
            peoplelist = self.retrieve_all()
            people = []
            for peep in peoplelist:
                people.append(peep.split(",")[0])
            return people
        except Exception as E:
            print(E)

    def retrieve_count(self):  # Retrieves the number of entries in the database (people in the queue)
        return len(self.retrieve_all())

    def find(self, uuid):
        try:
            if isUUID(uuid):
                ids = self.retrieve_uuid()
                index = ids.index(uuid)
                return index, len(ids)
            else:
                return None, None
        except ValueError as E:
            print(E)
            return

    def move(self, index, newindex):
        try:
            tomove = self.retrieve_all()
            if newindex >= len(tomove): newindex = len(tomove) - 1
            tomove.insert(newindex, tomove.pop(index))
            self.set_list(tomove)
        except Exception as E:
            print(E)

    def delete(self, delete):
        try:
            index = 0
            if isUUID(delete):
                index = int(self.find(delete)[0])
            elif isInt(delete):
                index = int(delete)
            else:
                return False
            popped = self.retrieve_all()
            popped.pop(index)
            self.set_list(popped)
            return True
        except Exception as E:
            print(E)
            return False

    def delete_all(self):
        try:
            self.Redis.delete("people")
        except Exception as E:
            print(E)
