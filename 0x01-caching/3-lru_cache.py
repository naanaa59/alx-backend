#!/usr/bin/env python3
""" class LRUCache that inherits from BaseCaching """
from collections import OrderedDict


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ class LRUCache that inherits from BaseCaching """
    def __init__(self):
        """ LRU init method"""
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """ LRU put method """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed_key, removed_item = self.cache_data.popitem(last=False)
            print(f"DISCARD: {removed_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ LIFO get method"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
