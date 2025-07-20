from pymongo import MongoClient

from config.config import get_config

global_session = None

class Session:
    def __init__(self, uri: str, database: str = "webglhost"):
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

def get_mongo_client():
    global global_session
    if global_session is None:
        config = get_config()
        mongo_config = config.get("mongo")
        host = mongo_config.get("host")
        port = mongo_config.get("port")
        username = mongo_config.get("user")
        password = mongo_config.get("password")
        database = mongo_config.get("database")

        mongo_uri = f'mongodb://{username}:{password}@{host}:{port}'
        session = Session(mongo_uri, database)
        global_session = session
        return global_session
    return global_session
