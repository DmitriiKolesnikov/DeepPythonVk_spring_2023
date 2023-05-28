import unittest
from logging import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_get_and_set(self):
        lru_cache = LRUCache(2)
        lru_cache.set(1, "one")
        lru_cache.set(2, "two")
        self.assertEqual(lru_cache.get(1), "one")
        lru_cache.set(3, "three")
        self.assertEqual(lru_cache.get(2), None)
        lru_cache.set(4, "four")
        self.assertEqual(lru_cache.get(1), None)
        self.assertEqual(lru_cache.get(3), "three")
        self.assertEqual(lru_cache.get(4), "four")

    def test_capacity(self):
        lru_cache = LRUCache(2)
        lru_cache.set(1, "one")
        lru_cache.set(2, "two")
        lru_cache.set(3, "three")
        self.assertEqual(lru_cache.get(1), None)
        self.assertEqual(lru_cache.get(2), "two")
        self.assertEqual(lru_cache.get(3), "three")
        lru_cache.set(4, "four")
        self.assertEqual(lru_cache.get(2), None)
        self.assertEqual(lru_cache.get(3), "three")
        self.assertEqual(lru_cache.get(4), "four")


if __name__ == '__main__':
    unittest.main()
