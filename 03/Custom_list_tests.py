from Custom_list import *
import unittest
a = CustomList([1, 2, 3, 4])
b = CustomList([2, 4, 9, 11, 3])
c = CustomList([0.2, 0.4, 0.7, 0.4])
d = CustomList([0.1, 0.3, 0.4])
f = CustomList(["dw", 2, 3, 5])
e = [2, 3, 5, 8, 9]


class TestCustomList(unittest.TestCase):

    def test__str__(self):
        self.assertEqual(a.__str__(), list([1, 2, 3, 4, 'Summa = 10']))
        self.assertEqual(b.__str__(), list([2, 4, 9, 11, 3, 'Summa = 29']))
        self.assertEqual(c.__str__(), list([0.2, 0.4, 0.7, 0.4, 'Summa = 1.7']))
        self.assertEqual(d.__str__(), list([0.1, 0.3, 0.4, 'Summa = 0.8']))

    def test_add(self):
        self.assertEqual(a + b, list([3, 6, 12, 15, 3]))
        self.assertEqual(a + c, list([1.2, 2.4, 3.7, 4.4]))
        self.assertEqual(a + d, list([1.1, 2.3, 3.4, 4]))
        self.assertEqual(a + e, list([3, 5, 8, 12, 9]))
        self.assertEqual(b + c, list([2.2, 4.4, 9.7, 11.4, 3]))
        self.assertEqual(b + d, list([2.1, 4.3, 9.4, 11, 3]))
        self.assertEqual(b + e, list([4, 7, 14, 19, 12]))
        self.assertEqual(c + d, list([0.3, 0.7, 1.1, 0.4]))
        self.assertEqual(c + e, list([2.2, 3.4, 5.7, 8.4]))
        self.assertEqual(d + e, list([2.1, 3.3, 5.4, 8, 9]))

    def test_sub(self):
        self.assertEqual(a - b, list([-1, -2, -6, -7, -3]))
        self.assertEqual(a - c, list([0.8, 1.6, 2.3, 3.6]))
        self.assertEqual(a - d, list([0.9, 1.7, 2.6, 4]))
        self.assertEqual(a - e, list([-1, -1, -2, -4, -9]))
        self.assertEqual(b - c, list([1.8, 3.6, 8.3, 10.6, 3]))
        self.assertEqual(b - d, list([1.9, 3.7, 8.6, 11, 3]))
        self.assertEqual(b - e, list([0, 1, 4, 3, -6]))
        self.assertEqual(c - d, list([0.1, 0.1, 0.3, 0.4]))
        self.assertEqual(c - e, list([-1.8, -2.6, -4.3, -7.6, -9]))
        self.assertEqual(d - e, list([-1.9, -2.7, -4.6, -8, -9]))

    def test_comparison(self):
        a1 = CustomList([1, 3, 3, 3])
        assert bool(a < b) == bool(sum([1, 2, 3, 4]) < sum([2, 4, 9, 11, 3])), False
        assert bool(b > a) == bool(sum([2, 4, 9, 11, 3]) > sum([1, 2, 3, 4])), False
        assert bool(b != a) == bool(sum([2, 4, 9, 11, 3]) != sum([1, 2, 3, 4])), False
        assert bool(a == a1) == bool(sum([1, 3, 3, 3]) == sum([1, 2, 3, 4])), False
        assert bool(a < e) == bool(sum([1, 2, 3, 4]) < sum([2, 3, 5, 8, 9])), False

    def test_instance(self):
        self.assertIsInstance(a + b, Customlist)
        self.assertIsInstance(a + e, CustomList)
        self.assertIsInstance(a - b, CustomList)
        self.assertIsInstance(a - e, CustomList)

    def test_permanence_of_custom_list(self):
        a1 = a
        b1 = b
        custom1 = a1 + b1
        self.assertIs(a, a1)
        self.assertIs(b, b1)
        c1 = c
        d1 = d
        custom2 = c1 + d1
        self.assertIs(c, c1)
        self.assertIs(d, d1)

    def test_comparison_correctly(self):
        self.assertEqual(bool(a < f), "Wrong type of i")
        self.assertEqual(bool(a > f), "Wrong type of i")
        self.assertEqual(bool(a != f), "Wrong type of i")
        self.assertEqual(bool(a == f), "Wrong type of i")


if "__name__" == __main__:
    print("CustomList tests are ready")
