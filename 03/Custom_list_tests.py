from Custom_list import *

a = CustomList([1, 2, 3, 4])
b = CustomList([2, 4, 9, 11, 3])
c = CustomList([0.2, 0.4, 0.7, 0.4])
d = CustomList([0.1, 0.3, 0.4])
f = CustomList(["dw", 2, 3, 5])
e = [2, 3, 5, 8, 9]


def check__str__():
    assert a.__str__() == list([1, 2, 3, 4, 'Summa = 10']), False
    assert b.__str__() == list([2, 4, 9, 11, 3, 'Summa = 29']), False
    assert c.__str__() == list([0.2, 0.4, 0.7, 0.4, 'Summa = 1.7']), False
    assert d.__str__() == list([0.1, 0.3, 0.4, 'Summa = 0.8']), False


def check_add():
    assert a + b == list([3, 6, 12, 15, 3]), False
    assert a + c == list([1.2, 2.4, 3.7, 4.4]), False
    assert a + d == list([1.1, 2.3, 3.4, 4]), False
    assert a + e == list([3, 5, 8, 12, 9]), False
    assert b + c == list([2.2, 4.4, 9.7, 11.4, 3]), False
    assert b + d == list([2.1, 4.3, 9.4, 11, 3]), False
    assert b + e == list([4, 7, 14, 19, 12]), False
    assert c + d == list([0.3, 0.7, 1.1, 0.4]), False
    assert c + e == list([2.2, 3.4, 5.7, 8.4, 9]), False
    assert d + e == list([2.1, 3.3, 5.4, 8, 9]), False


def check_sub():
    assert a - b == list([-1, -2, -6, -7, -3]), False
    assert a - c == list([0.8, 1.6, 2.3, 3.6]), False
    assert a - d == list([0.9, 1.7, 2.6, 4]), False
    assert a - e == list([-1, -1, -2, -4, -9]), False
    assert b - c == list([1.8, 3.6, 8.3, 10.6, 3]), False
    assert b - d == list([1.9, 3.7, 8.6, 11, 3]), False
    assert b - e == list([0, 1, 4, 3, -6]), False
    assert c - d == list([0.1, 0.1, 0.3, 0.4]), False
    assert c - e == list([-1.8, -2.6, -4.3, -7.6, -9]), False
    assert d - e == list([-1.9, -2.7, -4.6, -8, -9]), False


def check_comparison():
    a1 = CustomList([1, 3, 3, 3])
    assert bool(a < b) == bool(sum([1, 2, 3, 4]) < sum([2, 4, 9, 11, 3])), False
    assert bool(b > a) == bool(sum([2, 4, 9, 11, 3]) > sum([1, 2, 3, 4])), False
    assert bool(b != a) == bool(sum([2, 4, 9, 11, 3]) != sum([1, 2, 3, 4])), False
    assert bool(a == a1) == bool(sum([1, 3, 3, 3]) == sum([1, 2, 3, 4])), False
    assert bool(a < e) == bool(sum([1, 2, 3, 4]) < sum([2, 3, 5, 8, 9])), False
    
    
def check_instance():
    assert isinstance(a + b, CustomList) is True, False
    assert isinstance(a + e, CustomList) is True, False
    assert isinstance(a - b, CustomList) is True, False
    assert isinstance(a - e, CustomList) is True, False


def check_permanence_of_custom_list():
    a1 = a
    b1 = b
    custom1 = a1 + b1
    assert a is a1, False
    assert b is b1, False
    c1 = c
    d1 = d
    custom2 = c1 + d1
    assert c is c1, False
    assert d is d1, False


def check_comparison_correctly():
    assert bool(a < b) == "Wrong type of i", False
    assert bool(b > a) == "Wrong type of i", False
    assert bool(b != a) == "Wrong type of i", False
    assert bool(a == a1) == "Wrong type of i", False
    assert bool(a < e) == "Wrong type of i", False


if "__name__" == __main__:
    check_instance()
    check_comparison()
    check_sub()
    check_add()
    check_permanence_of_custom_list()
