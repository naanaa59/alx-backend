#!/usr/bin/env python3
"""  class BasicCache that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ class BasicCache that inherits from BaseCaching """

    def put(self, key, item):
        """assign self.cache_data the item value for the key key """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return
        return self.cache_data.get(key)
