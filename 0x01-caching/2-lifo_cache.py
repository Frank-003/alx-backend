#!/usr/bin/env python3
class BaseCaching:
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize the cache """
        self.cache_data = {}

class LIFOCache(BaseCaching):
    def __init__(self):
        """ Initialize the LIFO Cache """
        super().__init__()
        self.stack = []  # to keep track of the order of inserted keys

    def put(self, key, item):
        """ Add an item to the cache using LIFO algorithm """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop()  # get the last inserted key
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.stack.append(key)  # push the new key onto the stack

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)

