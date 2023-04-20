class LRUCache:
    count_dict = {}
    key_count = []
    dict_for_key_val = {}

    def __init__(self, maxsize):
        self.maxsize = maxsize

    def get(self, keys):

        if keys in self.count_dict.keys():
            if len(self.count_dict) <= self.maxsize:
                self.count_dict[keys] = max(self.count_dict.values()) + 1
                sorted_dict = {}
                sorted_keys = sorted(self.count_dict, key=self.count_dict.get)
                for w in sorted_keys:
                    sorted_dict[w] = self.count_dict[w]
                self.count_dict = sorted_dict
            else:
                key_to_del = []
                count_to_del = []
                value_to_del = []
                for key, count in self.count_dict.items():
                    key_to_del.append(key)
                    count_to_del.append(count)
                    value_to_del.append(self.dict_for_key_val[key])
                del key_to_del[0]
                del count_to_del[0]
                del value_to_del[0]
                self.count_dict = dict(zip(key_to_del, count_to_del))
                self.dict_for_key_val = dict(zip(key_to_del, value_to_del))
                #return f"{key_to_del, count_to_del}"

            return f"{self.dict_for_key_val[keys]}"
        else:
            return f"Such KEY has been deleted because of memory saving ,you can easy set this KEY again!"

    def set(self, key, value):
        if key not in self.dict_for_key_val.keys():
            if len(self.count_dict) <= self.maxsize:
                self.dict_for_key_val[key] = value
                self.key_count.append(key)
                if len(self.count_dict) < 1:
                    for k in self.key_count:
                        self.count_dict[k] = 0
                if len(self.count_dict) >= 1:
                    self.count_dict[key] = max(self.count_dict.values()) + 1
                sorted_dict = {}
                sorted_keys = sorted(self.count_dict, key=self.count_dict.get)
                for w in sorted_keys:
                    sorted_dict[w] = self.count_dict[w]
                self.count_dict = sorted_dict
            else:
                key_to_del = []
                count_to_del = []
                value_to_del = []
                for key, count in self.count_dict.items():
                    key_to_del.append(key)
                    count_to_del.append(count)
                    value_to_del.append(self.dict_for_key_val[key])
                del key_to_del[0]
                del count_to_del[0]
                del value_to_del[0]
                self.count_dict = dict(zip(key_to_del, count_to_del))
                self.dict_for_key_val = dict(zip(key_to_del, value_to_del))
            return f"{self.count_dict, self.dict_for_key_val}"
        else:
            return f"You hav already set this KEY and VALUE, check your data again"


if __name__ == "__main__":
    cache = LRUCache(2)

    (cache.set("k1", "val1"))
    (cache.set("k2", "val2"))

    print(cache.get("k3"))  # None
    print(cache.get("k2"))  # "val2"
    print(cache.get("k1"))  # "val1"
    #
    cache.set("k3", "val3")
    #
    print(cache.get("k3"))  # "val3"
    print(cache.get("k2"))  # None
    print(cache.get("k1"))  # "val1"
