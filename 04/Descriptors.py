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

