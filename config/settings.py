import os

mongo = {
    "dev": {
        "host": "localhost",
        "port": 27017,
        "database": "webglhost",
    }
}

redis = {
    "dev": {
        "host": "localhost",
        "port": 6379,
    }
}

config = {
    "mongo": mongo,
    "redis": redis,
}

ENV = 'dev'