from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # mark key as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # update if exists
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        self.cache[key] = value
        # evict least recently used
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)