from config.watchers.webglhost import PERMISSIONWINDOWS, INSTALL
from utils import mongo

watcher_collection = "watcher"

def insert_watcher_resource():
    mongo_client = mongo.get()

    mongo_client.insert_one(watcher_collection, PERMISSIONWINDOWS)
    mongo_client.insert_one(watcher_collection, INSTALL)

if __name__ == '__main__':
    insert_watcher_resource()