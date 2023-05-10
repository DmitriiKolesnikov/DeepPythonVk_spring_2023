import cProfile, pstats, io
import weakref
import time
N = int(10_000_000)


class UsualAttrBill:
    final_price_in_the_bill = {}

    def __init__(self, price, amount, dish_name, who_ordered):
        self.price = price
        self.amount = amount
        self.dish_name = dish_name
        self.who_ordered = who_ordered
        if isinstance(self.price, int) and isinstance(self.amount, int) and isinstance(self.dish_name, str)\
                and isinstance(who_ordered, list):
            pass
        else:
            print("False")

    def calc_check(self):
        final_price = self.price * self.amount
        self.final_price_in_the_bill[self.dish_name] = final_price
        return f"The bill looks like:{self.final_price_in_the_bill}"

    def __str__(self):
        return f"{self.price=}, {self.amount=}, {self.dish_name=}, {self.who_ordered}"


def take_usual_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


def change_usual_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            return lst[i]


def del_usual_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            del lst[i]


print("______________________________________________________________________________")
# start_time = time.time()
usual_attrs = [UsualAttrBill(2, 4, "qwerty", ["Баба", "Джо", "Алена"]) for _ in range(N)]
# print("--- %s seconds ---  took to create dict of usual attrs" % (time.time() - start_time))
# start_time = time.time()
# take_usual_attr(usual_attrs)
# print("--- %s seconds ---  took to get usual attr" % (time.time() - start_time))
# start_time = time.time()
# change_usual_attr(usual_attrs)
# print("--- %s seconds ---  took to change usual attr" % (time.time() - start_time))
# start_time = time.time()
# del_usual_attr(usual_attrs)
# print("--- %s seconds ---  took to del usual attr" % (time.time() - start_time))
print("______________________________________________________________________________")


class SlotsBill:
    final_price_in_the_bill = {}
    __slots__ = ["price", "amount", "bill", "dish_name", "who_ordered"]

    def __init__(self, price, amount, dish_name, who_ordered):
        self.price = price
        self.amount = amount
        self.dish_name = dish_name
        self.who_ordered = who_ordered
        if isinstance(self.price, int) and isinstance(self.amount, int) and isinstance(self.dish_name, str) \
                and isinstance(who_ordered, list):
            pass
        else:
            print("False")

    def final_list(self):
        final_list = []
        final_list.append(self.price)
        final_list.append(self.amount)
        final_list.append(self.who_ordered)
        self.final_price_in_the_bill[self.dish_name] = final_list
        return f"The bill looks like:{self.final_price_in_the_bill}"

    def __str__(self):
        return f"{self.final_price_in_the_bill} "


def take_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            return lst[i]


def change_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            return lst[i]


def del_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            del lst[i]


# start_time = time.time()
slot_attrs = [SlotsBill(2, 4, "qwerty", ["Баба", "Джо", "Алена"]) for _ in range(N)]
# print("--- %s seconds --- took to create dict of slotted attrs" % (time.time() - start_time))
# tart_time = time.time()
# take_slotted_attr(slot_attrs)
# print("--- %s seconds --- took to get slotted attrs" % (time.time() - start_time))
# start_time = time.time()
# change_slotted_attr(slot_attrs)
# print("--- %s seconds --- took to change slotted attrs" % (time.time() - start_time))
# start_time = time.time()
# del_slotted_attr(slot_attrs)
# print("--- %s seconds --- took to del slotted attrs" % (time.time() - start_time))
print("______________________________________________________________________________")


class WeakRefBill:
    final_price_in_the_bill = weakref.WeakKeyDictionary()

    def __init__(self, price, amount, dish_name, who_ordered):
        self.price = price
        self.amount = amount
        self.dish_name = dish_name
        self.who_ordered = who_ordered
        if isinstance(self.price, int) and isinstance(self.amount, int) and isinstance(self.dish_name, str)\
                and isinstance(self.who_ordered, list):
            pass
        else:
            print("False")

    def final_list(self):
        final_list = []
        final_list.append(self.price)
        final_list.append(self.amount)
        final_list.append(self.who_ordered)
        self.final_price_in_the_bill[self.dish_name] = final_list
        return f"The bill looks like:{self.final_price_in_the_bill}"

    def __str__(self):
        return f"{self.final_price_in_the_bill} "


def take_weakref_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


def change_weakreft_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


def del_weakref_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            del lst[i]


# start_time = time.time()
weakref_attrs = [WeakRefBill(2, 4, "qwerty", ["Баба", "Джо", "Алена"]) for _ in range(N)]
# print("--- %s seconds --- took to create dict of weakreffed attrs" % (time.time() - start_time))
# start_time = time.time()
# take_weakref_attr(weakref_attrs)
# print("--- %s seconds --- took to get weakreffed attr" % (time.time() - start_time))
# start_time = time.time()
# take_weakref_attr(weakref_attrs)
# print("--- %s seconds --- took to change weakreffed attr" % (time.time() - start_time))
# start_time = time.time()
# del_weakref_attr(weakref_attrs)
# print("--- %s seconds --- took to change weakreffed attr" % (time.time() - start_time))
print("______________________________________________________________________________")
print("Данные проведены с учетом того, что было создано 10 миллионов экземпляров каждого класса ")

# pr = cProfile.Profile()
# pr.enable()
# take_usual_attr(usual_attrs)
# change_usual_attr(usual_attrs)
# del_usual_attr(usual_attrs)
# take_slotted_attr(slot_attrs)
# change_slotted_attr(slot_attrs)
# del_slotted_attr(slot_attrs)
# take_weakref_attr(weakref_attrs)
# change_weakreft_attr(weakref_attrs)
# del_weakref_attr(weakref_attrs)
#
# pr.disable()
# s = io.StringIO()
# sortby = "cumulative"
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()

# print(s.getvalue())

print("----------------------------Используем декоратор------------------------")


def profile_deco(funk):
    import cProfile
    import pstats
    import io

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        return_value = funk(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return return_value
    return inner

@profile_deco
def take_usual_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


@profile_deco
def change_usual_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            return lst[i]


@profile_deco
def del_usual_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            del lst[i]


take_usual_attr(usual_attrs)
change_usual_attr(usual_attrs)
del_usual_attr(usual_attrs)

@profile_deco
def take_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            return lst[i]

@profile_deco
def change_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            return lst[i]

@profile_deco
def del_slotted_attr(lst):
    for i in range(len(lst)):
        if i == N - 1:
            lst[i] = "12345"
            del lst[i]


take_slotted_attr(slot_attrs)
change_slotted_attr(slot_attrs)
del_slotted_attr(slot_attrs)

@profile_deco
def take_weakref_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


@profile_deco
def change_weakreft_attr(lst):
    for i in range(len(lst)):
        if i == N-1:
            return lst[i]


@profile_deco
def del_weakref_attr_deco(lst):
    for i in range(len(lst)):
        if i == N-1:
            del lst[i]


take_weakref_attr(weakref_attrs)
change_slotted_attr(weakref_attrs)
del_weakref_attr_deco(weakref_attrs)
