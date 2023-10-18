#!/usr/bin/env python3
"""
   Implementing an expiring web cache and tracker 
"""
import requests
import redis
from functools import wraps


r = redis.Redis()


def access_count(method):
    """decorator for our function"""
    @wraps(method)
    def wrapper(url):
        """wrapper function"""
        key = "cached:" + url
        cached_value = r.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

        key_count = "count:" + url
        html_content = method(url)

        r.incr(key_count)
        r.set(key, html_content, ex=10)
        r.expire(key, 10)
        return html_content
    return wrapper


@access_count
def get_page(url: str) -> str:
    """obtains html content"""
    results = requests.get(url)
    return results.text
