#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching """
    
    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.order_of_access = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_item = self.order_of_access.pop()
                self.cache_data.pop(mru_item)
                print("DISCARD:", mru_item)
            self.cache_data[key] = item
            self.order_of_access.insert(0, key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.order_of_access.remove(key)
            self.order_of_access.insert(0, key)
            return self.cache_data[key]
        return None
