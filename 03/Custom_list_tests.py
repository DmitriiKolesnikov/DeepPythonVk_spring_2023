from Custom_list import *
import unittest


class TestCustomList(unittest.TestCase):
    def test_add_two_custom_lists(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([4, 5, 6])
        result = list1 + list2
        self.assertEqual(result, CustomList([5, 7, 9]))

    def test_add_custom_list_and_list(self):
        list1 = CustomList([1, 2, 3])
        list2 = [4, 5, 6]
        result = list1 + list2
        self.assertEqual(result, CustomList([5, 7, 9]))

    def test_add_list_and_custom_list(self):
        list1 = [1, 2, 3]
        list2 = CustomList([4, 5, 6])
        result = list1 + list2
        self.assertEqual(result, CustomList([5, 7, 9]))

    def test_subtract_two_custom_lists(self):
        list1 = CustomList([4, 5, 6])
        list2 = CustomList([1, 2, 3])
        result = list1 - list2
        self.assertEqual(result, CustomList([3, 3, 3]))

    def test_subtract_custom_list_and_list(self):
        list1 = CustomList([4, 5, 6])
        list2 = [1, 2, 3]
        result = list1 - list2
        self.assertEqual(result, CustomList([3, 3, 3]))


    def test_greater_than(self):
        list1 = CustomList([4, 5, 6])
        list2 = CustomList([1, 2, 3])
        self.assertGreater(list1, list2)
        self.assertFalse(list2 > list1)

    def test_greater_than_equal(self):
        list1 = CustomList([4, 5, 6])
        list2 = CustomList([1, 2, 3])
        self.assertGreaterEqual(list1, list2)
        self.assertGreaterEqual(list1, CustomList([4, 5, 6]))
        self.assertFalse(list2 >= list1)

    def test_less_than(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([4, 5, 6])
        self.assertLess(list1, list2)
        self.assertFalse(list2 < list1)

    def test_less_than_equal(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([4, 5, 6])
        self.assertLessEqual(list1, list2)
        self.assertLessEqual(list1, CustomList([1, 2, 3]))
        self.assertFalse(list2 <= list1)

    def test_string_representation(self):
        list1 = CustomList([1, 2, 3])
        self.assertEqual(str(list1), '[1, 2, 3] sum=6')


if __name__ == "__main__":
    unittest.main()

