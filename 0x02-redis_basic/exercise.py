#!/usr/bin/env python3
"""declares a redis class and methodS"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Union


def call_history(fn):
    """decorator to track method call history"""
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """returns the wrapper"""
        result = fn(self, *args, **kwargs)
        self._redis.lpush(f"{fn.__name__}_history", result)
        return result
    return wrapper

def call_count(fn):
    """decorator to track method call history"""
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        """returns the wrapper"""
        self._redis.incr(f"{fn.__name__}_count")
        return fn(self, *args, **kwargs)
    return wrapper


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get method that take a key string argument
           and an optional Callable argument named fn
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parametrizes Cache.get with the correct conversion function"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """parametrizes Cache.get with the correct conversion function"""
        return self.get(key, lambda x: int(x))
