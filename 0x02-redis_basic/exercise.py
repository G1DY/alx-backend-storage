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



def replay(fn: Callable):
    r = redis.Redis()
    function_name = fn.__qualname__
    count_key = f"{function_name}:count"
    value = r.get(count_key)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0

    print(f"{function_name} was called {value} times:")
    
    inputs_key = f"{function_name}:inputs"
    outputs_key = f"{function_name}:outputs"
    
    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)

    for input_str, output_str in zip(inputs, outputs):
        input_str = input_str.decode("utf-8")
        output_str = output_str.decode("utf-8")
        print(f"{function_name}(*{input_str}) -> {output_str}")
