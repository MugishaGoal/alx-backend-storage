#!/usr/bin/env python3
"""Module for retrieving HTML content from a URL and caching the result."""


import requests
import time
from functools import wraps


def cache_page(func):
    """
    Decorator to cache the result of a function with an expiration
    time of 10 seconds.
    """
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        url = args[0]
        if url in cache:
            if time.time() - cache[url]['timestamp'] < 10:
                return cache[url]['content']
            else:
                del cache[url]
        content = func(*args, **kwargs)
        cache[url] = {'content': content, 'timestamp': time.time()}
        return content

    return wrapper

@cache_page
def get_page(url: str) -> str:
    """Retrieve the HTML content of a URL and cache the result."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch content from {url}"
