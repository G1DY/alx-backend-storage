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
    def wrapper(url):
        """returns the decorator"""
        redis_client.incr(f"count:{url}")  # Increment the count for the URL
        count = int(redis_client.get(f"count:{url}") or 0)
        cached_response = redis_client.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis_client.setex(f"cached:{url}", 10, result)  # Cache the result with an expiration time of 10 seconds
        return result
    return wrapper


@response_cached_or_not
def get_page(url: str) -> str:
    """makes http request to a certain end point"""
    return get(url).text


if __name__ == "__main__":
    url = 'http://slowwly.robertomurray.co.uk'
    page_content = get_page(url)
    print("HTML Content:")
    print(page_content)
