# 0x01. Caching

## Resources
Read or watch:

* [Cache replacement policies - FIFO](https://intranet.alxswe.com/rltoken/fjhr6EvFeF3mWwsPQXUKdQ)
* [Cache replacement policies - LIFO](https://intranet.alxswe.com/rltoken/U44RQjXp8xBtsbNIyhHIyw)
* [Cache replacement policies - LRU](https://intranet.alxswe.com/rltoken/gKerxvR4dnXQYkBX2ujZiQ)
* [Cache replacement policies - MRU](https://intranet.alxswe.com/rltoken/Tmk4qEBZ7QTknvbpKabWfQ)
* [Cache replacement policies - LFU](https://intranet.alxswe.com/rltoken/8PEJ8L34bxhL2y--BW5zGQ)

## More Info

### Parent class BaseCaching

All your classes must inherit from BaseCaching defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```