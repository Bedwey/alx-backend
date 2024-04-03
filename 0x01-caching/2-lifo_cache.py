#!/usr/bin/env python3

"""
2-lifo_cache.py
Module that defines the class FIFOCache

Classes:
    LIFOCache
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class:
      - Inherits from BaseCaching
      - Uses a LIFO caching system
    """

    def put(self, key, item):
        """ Assign the item value for the key in self.cache_data dict.
        """
        if key is not None and item is not None:
            cacheLen = len(self.cache_data)
            if cacheLen >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last = list(self.cache_data.keys())[cacheLen - 1]
                print("DISCARD: {}".format(last))
                del self.cache_data[last]
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to key in self.cache_data dict.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
