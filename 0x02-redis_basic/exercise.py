#!/usr/bin/env python3
"""Cache class that interacts with Redis."""


import redis
import uuid
from typing import Union


class Cache:
    """Cache class interacts with Redis to store data"""
    def __init__(self):
        """Initialize the Cache instance with a Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis using the provided key and optionally apply a conversion function.

        Args:
            key: The key used to retrieve the data from Redis.
            fn: Optional conversion function to apply to the retrieved data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, optionally converted based on the provided function.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieve string data from Redis using the provided key"""
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """Retrieve integer data from Redis using the provided key"""
        return self.get(key, fn=int)
