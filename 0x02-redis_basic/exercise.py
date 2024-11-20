#!/usr/bin/env python3
import redis
import uuid
from typing import Callable, Optional, Union

class Cache:
    def __init__(self):
        """
        Initialize the Cache class by creating a Redis client instance and flushing the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key.

        Args:
            data (str, bytes, int, float): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The Redis key to retrieve.
            fn (Callable, optional): A callable to convert the data to the desired format.

        Returns:
            The data retrieved from Redis, with the conversion function applied if provided.
        """
        value = self._redis.get(key)
        if value is not None and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The Redis key to retrieve.

        Returns:
            str: The data retrieved from Redis as a string.
        """
        return self.get(key, lambda d: d.decode("utf-8") if isinstance(d, bytes) else d)

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The Redis key to retrieve.

        Returns:
            int: The data retrieved from Redis as an integer.
        """
        return self.get(key, lambda d: int(d) if d is not None else None)
