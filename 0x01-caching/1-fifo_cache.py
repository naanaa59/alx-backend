#!/usr/bin/env python3
"""class FIFOCache that inherits from BaseCaching  """

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching """
    def __ini__(self):
        """ Init method """
        super().__init__()

    def put(self, key, item):
        """ FIFO put method"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                and key not in self.cache_data:
            first_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ FIFO get method"""
        if key is None:
            return
        return self.cache_data.get(key)
