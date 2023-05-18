from Comparision import *
import cProfile
import pstats
import io

print("----------------------------Используем декоратор------------------------")


def custom_profile_deco(function):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        value_to_be_returned = function(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return value_to_be_returned
    return inner


@custom_profile_deco
def take_usual_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


@custom_profile_deco
def change_usual_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            return lst[i]


@custom_profile_deco
def del_usual_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            del lst[i]


take_usual_attr(usual_attrs)
change_usual_attr(usual_attrs)
del_usual_attr(usual_attrs)


@custom_profile_deco
def take_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            return lst[i]

@custom_profile_deco
def change_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            return lst[i]


@custom_profile_deco
def del_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            del lst[i]


# take_slotted_attr(slot_attrs)
# change_slotted_attr(slot_attrs)
# del_slotted_attr(slot_attrs)


@custom_profile_deco
def take_weakref_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


@custom_profile_deco
def change_weakreft_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


@custom_profile_deco
def del_weakref_attr_deco(lst):
    for i in range(len(lst)):
        if i == N-1:
            del lst[i]


# take_weakref_attr(weakref_attrs)
# change_slotted_attr(weakref_attrs)
# del_weakref_attr_deco(weakref_attrs)

print("------------------------Завершение работы декоратора---------------------")