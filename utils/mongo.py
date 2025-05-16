from typing import Any, Mapping

from pymongo import MongoClient
from pymongo.synchronous.cursor import Cursor

from config import settings
from config.settings import ENV

global_session = None

class Session:
    def __init__(self, uri: str, database: str = "test"):
        self.client = MongoClient(uri)
        self.db = self.client[database]

    def c(self, collection: str):
        return self.db.get_collection(collection)

    def find_one(self, collection: str, query: dict):
        res = self.c(collection).find_one(query)
        return res

    def insert_one(self, collection: str, data: dict):
        res = self.c(collection).insert_one(data)
        return res

    def find_all(self, collection: str, query: dict):
        res = self.c(collection).find(query)
        return list(res)

def get():
    global global_session
    if global_session is None:
        config = settings.config['mongo'][ENV]
        host = config['host']
        port = config['port']
        database = config['database']
        mongo_uri = f'mongodb://{host}:{port}'
        session = Session(mongo_uri, database)
        global_session = session
        return global_session
