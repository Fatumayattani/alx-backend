#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching """
    
    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()
        self.order_of_insertion = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_item = self.order_of_insertion[0]
                self.cache_data.pop(first_item)
                self.order_of_insertion.pop(0)
                print("DISCARD:", first_item)
            self.cache_data[key] = item
            self.order_of_insertion.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
