#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps
from typing import Callable


store = redis.Redis()


def count_url_access(method: Callable) -> Callable:
    """ Decorator counting how many times
    a URL is accessed """
    @wraps(method)
    def wrapper(url):
        store.incr(f'count:{url}')
        result = store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        store.set(f'count:{url}', 0)
        store.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
