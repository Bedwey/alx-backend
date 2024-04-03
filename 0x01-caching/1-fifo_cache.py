#!/usr/bin/env python3

"""
1-fifo_cache.py
Module that defines the class FIFOCache

Classes:
    FIFOCache
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class:
      - Inherits from BaseCaching
      - Uses a FIFO caching system
    """

    def put(self, key, item):
        """ Adds an item in the cache.
            If the cache is full, it uses the FIFO 
            algorithm to remove the last item.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    first = list(self.cache_data.keys())[0]
                    print("DISCARD: {}".format(first))
                    del self.cache_data[first]
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to key in self.cache_data dict.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
