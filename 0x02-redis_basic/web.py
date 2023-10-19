#!/usr/bin/env python3
"""
web cache and tracker
"""
from requests import get
import redis
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def response_cached_or_not(fn: Callable) -> Callable:
    """a decorator to cache a http request in redis"""
    @wraps(fn)
    def response_cached_or_not(fn: Callable) -> Callable:
    """a decorator to cache a http request in redis"""
    @wraps(fn)
    def wrapper(url):
        """returns the decorator"""
        redis_client.incr(f"count:{url}")
        cached_response = redis_client.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis_client.setex(f"cached:{url}", 10, result)
        return result
    return wrapper


@response_cached_or_not
def get_page(url: str) -> str:
    """makes http request to a certain end point"""
    return get(url).txt
