#!/usr/bin/env python3

"""
3-lru_cache.py
Module that defines the class LRUCache

Classes:
    LRUCache
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LIFOCache class:
      - Inherits from BaseCaching
      - Uses a LIFO caching system
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Adds an item in the cache.
            If the cache is full, it uses the LRU
            algorithm to remove the least recently used item.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.keys.pop(0)
            self.cache_data.pop(discard)
            print(f"DISCARD: {discard}")
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """ Return the value linked to key in self.cache_data dict.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
