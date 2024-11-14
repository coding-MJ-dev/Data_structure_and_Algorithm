# 146. LRU Cache

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.key2val:
            self.key2val.move_to_end(key)
            return self.key2val[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key2val:
            self.key2val[key] = value
            self.key2val.move_to_end(key)
        else:
            self.key2val[key] = value
            if len(self.key2val) > self.cap:
                self.key2val.popitem(last=False)