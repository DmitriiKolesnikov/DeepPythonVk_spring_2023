import unittest
from LRU_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(limit=2)

    def test_get_non_existent_key(self):
        self.assertIsNone(self.cache.get('non_existent_key'))

    def test_set_and_get_single_key(self):
        self.cache.set('key1', 'value1')
        self.assertEqual(self.cache.get('key1'), 'value1')

    def test_replace_existing_key(self):
        self.cache.set('key1', 'value1')
        self.cache.set('key1', 'value2')
        self.assertEqual(self.cache.get('key1'), 'value2')

    def test_trim_cache(self):
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        self.cache.set('key3', 'value3')
        self.assertIsNone(self.cache.get('key1'))

    def test_order_of_access(self):
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        self.assertEqual(self.cache.get('key1'), 'value1')
        self.cache.set('key3', 'value3')
        self.assertIsNone(self.cache.get('key2'))

    def test_key_overflow(self):
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        self.cache.set('key3', 'value3')
        self.assertIsNone(self.cache.get('key1'))

    def test_key_order(self):
        self.cache.set('key1', 'value1')
        self.cache.set('key2', 'value2')
        self.assertEqual(self.cache.get('key1'), 'value1')
        self.cache.set('key3', 'value3')
        self.cache.set('key2', 'value2_2')
        self.assertIsNone(self.cache.get('key1'))


class TestLRUCacheLimitOne(unittest.TestCase):
    def setUp(self):
        self.cache1 = LRUCache(limit=1)

    def test_get_non_existent_key(self):
        self.assertIsNone(self.cache1.get('non_existent_key'))

    def test_set_and_get_single_key(self):
        self.cache1.set('key1', 'value1')
        self.assertEqual(self.cache1.get('key1'), 'value1')

    def test_replace_existing_key(self):
        self.cache1.set('key1', 'value1')
        self.cache1.set('key1', 'value2')
        self.assertEqual(self.cache1.get('key1'), 'value2')

    def test_trim_cache(self):
        self.cache1.set('key1', 'value1')
        self.cache1.set('key2', 'value2')
        self.assertIsNone(self.cache1.get('key1'))

    def test_order_of_access(self):
        self.cache1.set('key1', 'value1')
        self.cache1.set('key2', 'value2')
        self.assertEqual(self.cache1.get('key2'), 'value2')
        self.cache1.set('key3', 'value3')
        self.assertIsNone(self.cache1.get('key1'))

    def test_key_overflow(self):
        self.cache1.set('key1', 'value1')
        self.cache1.set('key2', 'value2')
        self.cache1.set('key3', 'value3')
        self.assertIsNone(self.cache1.get('key1'))

    def test_key_order(self):
        self.cache1.set('key1', 'value1')
        self.cache1.set('key2', 'value2')
        self.cache1.set('key3', 'value3')
        self.assertEqual(self.cache1.get('key3'), 'value3')
        self.assertIsNone(self.cache1.get('key1'))


if __name__ == '__main__':
    unittest.main()
