#!/usr/bin/env python3
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        return self.cache_data.get(key, None)

