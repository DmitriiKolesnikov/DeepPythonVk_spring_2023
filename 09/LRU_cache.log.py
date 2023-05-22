import logging
from collections import OrderedDict


class CustomFilter(logging.Filter):
    def filter(self, record):
        return len(record.getMessage().split()) % 2 == 1


logging.basicConfig(filename='LRU_cache.log.py', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)

filter = CustomFilter()

root_logger = logging.getLogger()
root_logger.addHandler(console_handler)
root_logger.addFilter(filter)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            logging.warning(f'Key {key} not found')
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        logging.debug(f'Get key {key}: {value}')
        return value

    def set(self, key, value):
        if key in self.cache:
            logging.debug(f'Set key {key}: {value}')
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            logging.debug(f'Cache is full, remove key {next(iter(self.cache))}')
            self.cache.popitem(last=False)
        logging.debug(f'Set key {key}: {value}')
        self.cache[key] = value


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='LRU Cache with logging')
    parser.add_argument('-s', action='store_true', help='Log to stdout')
    parser.add_argument('-f', action='store_true', help='Use custom filter')
    args = parser.parse_args()

    logging.basicConfig(filename='LRU_cache.log.py', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s')

    if args.s:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')
        console_handler.setFormatter(console_formatter)
        root_logger = logging.getLogger()
        root_logger.addHandler(console_handler)

    if args.f:
        class CustomFilter(logging.Filter):
            def filter(self, record):
                return len(record.getMessage().split()) % 2 == 1

        filter = CustomFilter()
        root_logger = logging.getLogger()
        root_logger.addFilter(filter)

    cache = LRUCache(2)
    cache.set(1, 1)
    cache.set(2, 2)
    cache.get(1)
    cache.set(3, 3)
    cache.get(2)
    cache.set(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)

