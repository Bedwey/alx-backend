#!/usr/bin/env python3

"""
100-lfu_cache.py
Module that defines the class LFUCache

Classes:
    LFUCache
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class:
      - Inherits from BaseCaching
      - Uses a LFU caching system
    """

    def __init__(self):
        """ Initializes the LFUCache instance. """
        super().__init__()
        self.keys = []
        self.counts = {}

    def put(self, key, item):
        """ Adds an item in the cache.
            If the cache is full, it uses the LFU
            algorithm to remove the least frequent item.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys.remove(key)
            self.counts[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                least_frequent_key = min(self.counts, key=self.counts.get)
                self.keys.remove(least_frequent_key)
                self.cache_data.pop(least_frequent_key)
                self.counts.pop(least_frequent_key)
                print(f"DISCARD: {least_frequent_key}")
            self.counts[key] = 1
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Return the value linked to key in self.cache_data dict.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
