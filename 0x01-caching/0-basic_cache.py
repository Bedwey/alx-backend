#!/usr/bin/env python3

'''Task 0: Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class:
      - Inherits from BaseCaching
      - Has no limit
    """

    def put(self, key, item):
        """ Assign the item value for the key in self.cache_data dict.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to key in self.cache_data dict.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
