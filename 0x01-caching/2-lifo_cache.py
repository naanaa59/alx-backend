#!/usr/bin/env python3
"""class LIFOCache that inherits from BaseCaching  """

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ class LIFOCache that inherits from BaseCaching """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ LIFO Caching put method"""
        if key is None or item is None:
            return
        max = BaseCaching.MAX_ITEMS
        if key in self.cache_data:
            self.cache_data.pop(key)
            # print(f"DISCARD: {key}")
        elif len(self.cache_data) >= max:
            removed_key, removed_val = self.cache_data.popitem()
            print(f"DISCARD: {removed_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ LIFO get method"""
        if key is None:
            return
        return self.cache_data.get(key)
