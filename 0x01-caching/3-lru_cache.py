#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching """
    
    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.order_of_insertion = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_item = self.order_of_insertion.pop()
                self.cache_data.pop(last_item)
                print("DISCARD:", last_item)
            self.cache_data[key] = item
            self.order_of_insertion.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
