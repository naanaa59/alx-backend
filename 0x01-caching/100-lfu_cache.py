#!/usr/bin/env python3
"""   class LFUCache: the least frequency used item (LFU algorithm)"""
from collections import Counter

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Class hat inherits from BaseCaching and is a caching system """
    def __init__(self):
        """ LFUClass init method"""
        super().__init__()
        self.f_counter = Counter(self.cache_data)

    def put(self, key, item):
        """ LFU put method """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            sorted_counter = sorted(self.f_counter.items(), key=lambda x: x[1])
            if sorted_counter:
                lfu_k = sorted_counter[0][0]
                # print(self.cache_data)
                # print(self.f_counter)
                self.cache_data.pop(lfu_k)
                self.f_counter.pop(lfu_k)
                # print(self.cache_data)
                # print(self.f_counter)
                print(f"DISCARD: {lfu_k}")
        self.cache_data[key] = item
        self.f_counter[key] += 1

    def get(self, key):
        """ LFU get method"""
        if key is None or key not in self.cache_data:
            return None
        self.f_counter[key] += 1
        return self.cache_data[key]
