#!/usr/bin/env python3
"""declares a redis class and methodS"""
import redis
from uuid import uuid4


class Cache:
    """declares a cache redis class"""
    def __init__(self):
        """stores an instance and flush"""
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @call_count
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string"""
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey
