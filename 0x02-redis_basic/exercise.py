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
