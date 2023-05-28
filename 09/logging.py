import logging


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.logger = logging.getLogger(__name__)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            self.logger.info("Accessed element with key (%s) and value (%s)", key, node.value)
            return node.value
        else:
            self.logger.info("Element with key (%s) not found", key)
            return None

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
            self.logger.debug("Updated element with key (%s) and new value (%s)", key, value)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)
            if len(self.cache) > self.capacity:
                node_to_remove = self.head.next
                self._remove(node_to_remove)
                del self.cache[node_to_remove.key]
                self.logger.info("Removed element with key (%s) and value (%s) due to capacity", node_to_remove.key, node_to_remove.value)
            self.logger.debug("Added new element with key (%s) and value (%s)", key, value)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    lru_cache = LRUCache(2)
    lru_cache.set(1, "one")
    lru_cache.set(2, "two")
    lru_cache.get(1)
    lru_cache.set(3, "three")
    lru_cache.get(2)
    lru_cache.set(4, "four")
    lru_cache.get(1)
    lru_cache.get(3)
    lru_cache.get(4)
