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
