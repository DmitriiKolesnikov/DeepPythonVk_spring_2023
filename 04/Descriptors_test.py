from Descriptors import *
import unittest


class TestDescriptors(unittest.TestCase):

    def test_menu_str(self):
        self.assertEqual(Menu(1, "qwer", 10).__str__(), "position is №1, name = Qwer, price = 10$")
        self.assertEqual(Menu(2, "qwerty", 12).__str__(), "position is №2, name = Qwerty, price = 12$")

    def test_menu_errors(self):
        self.assertRaises(ValueError, Menu, 0.1, "qwer", 12)
        self.assertRaises(ValueError, Menu, 0.8, "1we", 10)
        self.assertRaises(ValueError, Menu, 10, 23, 10)
        self.assertRaises(ValueError, Menu, 10, 12, 12)
        self.assertRaises(ValueError, Menu, 10, "qwer", -1)
        self.assertRaises(ValueError, Menu, 10, "qwer", -10)

    def test_del_in_descriptors(self):
        a = Menu(1, "qwer", 1)
        del a.position
        a.position = 2
        self.assertEqual(a.__str__(), "position is №2, name = Qwer, price = 1$")
        del a.name
        a.name = "qwer1"
        self.assertEqual(a.__str__(), "position is №2, name = Qwer1, price = 1$")
        del a.price
        a.price = 10
        self.assertEqual(a.__str__(), "position is №2, name = Qwer1, price = 10$")


if __name__ == "__main__":
    unittest.main()
