#!/usr/bin/env python3
"""Create a Cache class. In the __init__ method, store an instance
   of the Redis client as a private variable named _redis (using 
   redis.Redis()) and flush the instance using flushdb

   In this exercise we will create a get method that take a key 
   string argument and an optional Callable argument named fn. 
   This callable will   be used to convert the data back to the desired format

   Create and return function that increments the count for that key every 
   time the method is called and returns the value returned by the original

   In call_history, use the decorated function’s qualified name and append
   ":inputs" and ":outputs" to create input and output list keys, respectively.

   In this tasks, we will implement a replay function to display the history
   of calls of a particular function.
"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """A decorator to count how many times a method is called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Increment the count for the method key in Redis
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls  # Decorate the store method with count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
