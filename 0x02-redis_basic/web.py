#!/usr/bin/env python3
"""implement redis that retrieves html"""
import requests
import redis
from functools import wraps


# Initialize a Redis connection
redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)


def cache_result(method):
    @wraps(method)
    def wrapper(url):
        # Check if the result is cached
        cached_result = redis_conn.get(f"cache:{url}")
        if cached_result:
            return cached_result.decode("utf-8")

        # If not cached, fetch the result and cache it
        result = method(url)
        redis_conn.setex(f"cache:{url}", 10, result)
        return result

    return wrapper

def get_page(url):
    # Simulate slow response from http://slowwly.robertomurray.co.uk
    slow_url = f"http://slowwly.robertomurray.co.uk/delay/5000/url/{url}"

    response = requests.get(slow_url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to fetch URL: {url}"

# Apply caching decorator
get_page = cache_result(get_page)
