from typing import Optional, Dict

import redis


class RedisClient:
    def __init__(self, host: str, port: int):
        self.base_name_space = None
        self.pools: Dict[str, redis.Redis] = {}
        self.connections: Dict[str, redis.Redis] = {}
        self.client: Optional[redis.Redis] = None
        self.dbs = {
            'default': 0,
        }
        self.host = host
        self.port = port

    def connect(self):
        """创建所有的连接池"""
        try:
            for name, db in self.dbs.items():
                self.connections[name] = redis.Redis(
                    host=self.host,
                    port=self.port,
                    db=db,
                    decode_responses=True
                )
                if not self.connections[name].ping():
                    raise ConnectionError(f"Failed to connect to Redis db {db}")

            print(f"Connected to Redis at {self.host}:{self.port}")
        except Exception as e:
            raise ConnectionError(f"Redis connection failed: {str(e)}")

    def use_db(self, db_name: str):
        """
        获取指定db连接并返回自身以支持链式调用
        """
        if db_name not in self.connections:
            raise ValueError(f"Unknown db name: {db_name}")

        self.client = self.connections[db_name]

    def set_base_namespace(self, namespace: str):
        self.base_name_space = namespace

    def push_tail(self, key: str, value: str, timeout: int = 36000) -> int:
        try:
            key = f"{self.base_name_space}:{key}"
            result = self.client.rpush(key, value)
            self.client.expire(key, timeout)
            return result
        except Exception as e:
            raise RuntimeError(f"Redis LPUSH failed: {str(e)}")

    def get_list_range(self, key: str, start: int, end: int) -> list:
        try:
            key = f"{self.base_name_space}:{key}"
            return [item for item in self.client.lrange(key, start, end)]
        except Exception as e:
            raise RuntimeError(f"Redis LRANGE failed: {str(e)}")

    def get_list_all(self, key: str) -> list:
        return self.get_list_range(key, 0, -1)

    def close(self):
        for conn in self.connections.values():
            conn.close()
        self.connections.clear()
        self.client = None
