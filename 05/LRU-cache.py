
class LRUCache:
    LRU_dict = {}

    def __init__(self, limit):
        if isinstance(limit, int):
            self.limit = limit
        elif isinstance(limit, float):
            limit = round(limit)
            self.limit = limit
        else:
            raise ValueError

    def get(self, key):
        if key not in self.LRU_dict.keys():
            return None
        if key in self.LRU_dict.keys():
            value = self.LRU_dict[key]
            self.LRU_dict[key] = value
            del self.LRU_dict[key]
            self.LRU_dict[key] = value
            return value

    def set(self, key, value):
        self.LRU_dict[key] = value
        if len(self.LRU_dict) <= self.limit:
            return self.LRU_dict
        else:
            self.LRU_dict = dict(reversed(self.LRU_dict.items()))
            self.LRU_dict.popitem()
            self.LRU_dict = dict(reversed(self.LRU_dict.items()))
            return self.LRU_dict

    def __str__(self):
        return f"{self.LRU_dict}"
