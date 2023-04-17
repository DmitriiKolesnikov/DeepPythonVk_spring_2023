from MyMeta import *
import unittest


class TestMyMeta(unittest.TestCase):
    dimes = User()

    def test_instance(self):
        self.assertIsInstance(dimes, User)
        self.assertEqual(hasattr(dimes, "custom_x"), True)
        self.assertEqual(hasattr(dimes, "custom_val"), True)
        self.assertEqual(hasattr(dimes, "custom_line"), True)

    def test_examples(self):
        self.assertEqual(dimes.custom_x, 50)
        self.assertEqual(dimes.custom_val, 99)
        self.assertEqual(dimes.custom_line, 100)
        self.assertEqual(dimes.__str__(), "Custom_by_metaclass")
        dimes.dynamic = "added later"
        self.assertEqual(dimes.cutom_dynamic, "added later")
        self.assertNotEqual(dimes.dynamic, "added later")

    def test_not_instance(self):
        self.assertEqual(hasattr(dimes, "x"), True)
        self.assertEqual(hasattr(dimes, "val"), True)
        self.assertEqual(hasattr(dimes, "line"), True)

