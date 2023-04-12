class MyMeta(type):

    def __new__(mcs, name, bases, attrs):
        new_attrs = {}
        for key, value in attrs.items():
            new_key = "custom_" + key
            new_attrs[new_key] = value
        cls = super().__new__(mcs, name, bases, new_attrs)
        return cls

    def __init__(cls, name, bases, attrs):
        new_attrs = {}
        for key, value in attrs.items():
            new_key = "custom_" + key
            new_attrs[new_key] = value
        super().__init__(name, bases, new_attrs)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return {'b': 2, 'a': 5}


class User(metaclass=MyMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def sum(self):
        print("summa")

    def __str__(self):
        return "Custom_by_metaclass"


def test_first_task():
    inst = User()
    assert inst.custom_x == 50, False
    assert inst.custom_val == 99, False
    assert inst.custom_line() == 100, False
    assert str(inst) == "Custom_by_metaclass", False
    assert inst.x == 50, False
    assert inst.val == 99, False
    assert inst.line() == 100, False
    inst.dynamic = "added later"
    assert inst.custom_dynamic == "added later", False
    assert inst.dynamic == "added later", False


class Integer:

    def __set_name__(self, owner, integer_number):
        self.integer_number = integer_number
        self._protected_integer_number = f"_{integer_number}"

    def __get__(self, obj, objtype):
        return getattr(obj, self._protected_integer_number)

    def __set__(self, obj, value):
        if isinstance(value, int):
            return setattr(obj, self._protected_integer_number, value)
        else:
            raise TypeError("Type of number mast be Integer!")

    def __delete__(self, obj):
        print("delete from", obj)
        delattr(obj, self._protected_integer_number)


class String:

    def __set_name__(self, owner, string_name):
        self.string_name = string_name
        self._protected_string_name = f"_{string_name}"

    def __get__(self, obj, objtype):
        return getattr(obj, self._protected_string_name)

    def __set__(self, obj, val):
        if isinstance(val, str):
            return setattr(obj, self._protected_string_name, val)
        else:
            raise TypeError("Type of the object must be string!")

    def __delete__(self, obj):
        print("delete from", obj)
        delattr(obj, self._protected_string_name)


class PositiveInteger:

    def __set_name__(self, owner, positive_integer_name):
        self.positive_integer_name = positive_integer_name
        self._protected_positive_integer_name = f"_{positive_integer_name}"

    def __get__(self, obj, objtype):
        return getattr(obj, self._protected_positive_integer_name)

    def __set__(self, obj, val):
        if isinstance(val, int) and val >= 0:
            return setattr(obj, self._protected_positive_integer_name, val)
        else:
            raise ValueError("The Price must be >= 0!")

    def __delete__(self, obj):
        print("delete from", obj)
        delattr(obj, self._protected_positive_integer_name)


class Menu:
    position = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, position, name, price):
        self.position = position
        self.name = name
        self.price = price

    def __str__(self):
        return f"position is №{self.position}, name = {self.name.title()}, price = {self.price}$"


def test_second_task():
    pass