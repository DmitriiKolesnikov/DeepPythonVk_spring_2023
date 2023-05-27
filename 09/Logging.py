
import logging
import argparse

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru_list = []

    def get(self, key):
        if key in self.cache:
            self.lru_list.remove(key)
            self.lru_list.append(key)
            return self.cache[key]
        else:
            return "Key not found"

    def set(self, key, val):
        if key in self.cache:
            self.lru_list.remove(key)
        elif len(self.lru_list) >= self.capacity:
            evicted_key = self.lru_list.pop(0)
            self.cache.pop(evicted_key)
        self.cache[key] = val
        self.lru_list.append(key)

def main(args):
    logging_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(filename='cache.log', format=logging_format, level=logging_level)

    if args.stdout:
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter('%(message)s'))
        logging.getLogger('').addHandler(console)

    if args.filter == "even":
        filter_func = lambda record: len(record.getMessage().split())%2 == 0
    else:
        filter_func = None

    if filter_func:
        logging.getLogger('').addFilter(logging.Filter()(filter_func))

    cache = LRUCache(args.capacity)
    cache.set(1, "one")
    logging.info(f"Set key 1 to value 'one'")
    cache.set(2, "two")
    logging.info(f"Set key 2 to value 'two'")
    logging.debug("This is a debug message")
    val = cache.get(1)
    logging.info(f"Getting value for key 1: {val}")
    val = cache.get(3)
    logging.info(f"Getting value for key 3: {val}")
    cache.set(3, "three")
    logging.info(f"Set key 3 to value 'three'")
    cache.set(4, "four")
    logging.info(f"Set key 4 to value 'four'")
    cache.set(5, "five")
    logging.info(f"Set key 5 to value 'five'")
    cache.set(6, "six")
    logging.info(f"Set key 6 to value 'six'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--capacity", type=int, default=5, help="capacity of the cache")
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug logging")
    parser.add_argument("-s", "--stdout", action="store_true", help="log to stdout with separate formatting")
    parser.add_argument("-f", "--filter", choices=["even", "odd"], help="custom filter to apply to log records")
    args = parser.parse_args()

    main(args)
