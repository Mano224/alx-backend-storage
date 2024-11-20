#!/usr/bin/env python3
import uuid
import redis
from typing import Union

class Cache:
    """
        Initialize the Cache class by creating a Redis client instance and flushing the database.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        rando_key = str(uuid.uuid4())
        self._redis.set(rando_key, data)
        return rando_key

        
