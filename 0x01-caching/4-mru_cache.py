#!/usr/bin/env python3

"""
4-mru_cache.py
Module that defines the class MRUCache

Classes:
    MRUCache
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class:
      - Inherits from BaseCaching
      - Uses a MRU caching system
    """

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Adds an item in the cache.
            If the cache is full, it uses the LIFO
            algorithm to remove the last item.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.keys.pop()
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
