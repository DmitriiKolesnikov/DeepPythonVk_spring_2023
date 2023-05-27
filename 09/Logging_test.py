import unittest
from Logging import LRUCache

class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)

    def test_get_existing_key(self):
        self.cache.set(1, "one")
        self.assertEqual(self.cache.get(1), "one")

    def test_get_missing_key(self):
        self.assertEqual(self.cache.get(1), "Key not found")

    def test_set_existing_key(self):
        self.cache.set(1, "one")
        self.cache.set(1, "new_one")
        self.assertEqual(self.cache.get(1), "new_one")

    def test_set_missing_key(self):
        self.cache.set(1, "one")
        self.cache.set(2, "two")
        self.cache.set(3, "three")
        self.cache.set(4, "four")
        self.assertEqual(self.cache.get(1), "Key not found")
        self.assertEqual(self.cache.get(2), "two")
        self.assertEqual(self.cache.get(3), "three")
        self.assertEqual(self.cache.get(4), "four")

    def test_peek(self):
        self.cache.set(1, "one")
        self.assertEqual(len(self.cache.cache), 1)
        self.assertEqual(len(self.cache.lru_list), 1)
        self.assertEqual(self.cache.lru_list[-1], 1)
        self.cache.set(2, "two")
        self.assertEqual(len(self.cache.cache), 2)
        self.assertEqual(len(self.cache.lru_list), 2)
        self.assertEqual(self.cache.lru_list[-1], 2)
        self.cache.set(3, "three")
        self.assertEqual(len(self.cache.cache), 3)
        self.assertEqual(len(self.cache.lru_list), 3)
        self.assertEqual(self.cache.lru_list[-1], 3)
        self.cache.get(1)
        self.assertEqual(len(self.cache.cache), 3)
        self.assertEqual(len(self.cache.lru_list), 3)
        self.assertEqual(self.cache.lru_list[-1], 1)

if __name__ == '__main__':
    unittest.main()
