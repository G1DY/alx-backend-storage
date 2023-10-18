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


def call_history(method: Callable) -> Callable:
    """A decorator to store the history of inputs and outputs for a method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Create keys for input and output lists
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Normalize input arguments to strings
        input_str = str(args)

        # Use Redis RPUSH to append input arguments to the inputs list
        self._redis.rpush(inputs_key, input_str)

        # Call the original method to retrieve the output
        output = method(self, *args, **kwargs)

        # Normalize the output to a string
        output_str = str(output)

        # Use Redis RPUSH to append the output to the outputs list
        self._redis.rpush(outputs_key, output_str)

        # Return the output
        return output

    return wrapper

class Cache:
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history  # Decorate the store method with call_history
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

