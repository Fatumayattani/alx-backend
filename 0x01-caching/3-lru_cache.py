#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching """
    
    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.order_of_access = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lru_item = self.order_of_access.pop(0)
                self.cache_data.pop(lru_item)
                print("DISCARD:", lru_item)
            self.cache_data[key] = item
            self.order_of_access.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.order_of_access.remove(key)
            self.order_of_access.append(key)
            return self.cache_data[key]
        return None
