from LRU_cache import *
import unittest


class TestLRUCache(unittest.TestCase):

    def test_init(self):
        limit = 5
        lru = LRUCache(limit)
        self.assertEqual(lru.limit, limit)

    def test_get_not_in_lru(self):
        lru = LRUCache(5)
        self.assertIsNone(lru.get('key'))

    def test_get_in_lru(self):
        lru = LRUCache(5)
        lru.LRU_dict = {'key': 'value'}
        self.assertEqual(lru.get('key'), 'value')

    def test_set_in_lru_length_under_limit(self):
        lru = LRUCache(5)
        lru.LRU_dict = {'key': 'value'}
        self.assertEqual(lru.set('key2', 'value2'), {'key': 'value', 'key2': 'value2'})

    def test_set_in_lru_length_over_limit(self):
        lru = LRUCache(1)
        lru.LRU_dict = {'key': 'value'}
        self.assertEqual(lru.set('key2', 'value2'), {'key2': 'value2'})


if __name__ == "__main__":
    unittest.main()

    cache = LRUCache(2)

    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    assert cache.get("k3") == "val3"
    assert cache.get("k2") is None
    assert cache.get("k1") == "val1"
