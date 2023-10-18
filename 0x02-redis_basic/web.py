#!/usr/bin/env python3
"""
   Implementing an expiring web cache and tracker 
"""
import requests
import redis


# Initialize the Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)


def get_page(url: str) -> str:
    # Define the key for counting access to this URL
    count_key = f"count:{url}"
    # Try to get the access count from Redis
    access_count = redis_client.get(count_key)
    
    if access_count is None:
        access_count = 0
    else:
        access_count = int(access_count)
    
    # If the count exceeds 10, reset the count to 0 and get the page
    if access_count >= 10:
        access_count = 0

    # Increment the access count
    redis_client.set(count_key, access_count + 1)

    # Define the cache key for the page content
    cache_key = f"cache:{url}"
    cached_page = redis_client.get(cache_key)

    if cached_page is not None:
        # If the page is in the cache, return it
        return cached_page.decode("utf-8")
    else:
        # If not in the cache, fetch the page
        response = requests.get(url)
        page_content = response.text

        # Cache the page content with a 10-second expiration
        redis_client.setex(cache_key, 10, page_content)

        return page_content
