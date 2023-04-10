
class CustomList(list):

    def __init__(self, data):
        super(CustomList, self).__init__()
        self.list = []
        if data:
            self.list = list(data)

    def __str__(self):
        summa = 0
        for i in self.list:
            if type(i) == int:
                summa += i
            elif type(i) == float:
                summa += round(i, 3)
            else:
                return f"Unexpected type of data. Check your CustomList"
        summa = str(summa)
        res_sum = "Summa = " + summa
        self.list.append(res_sum)
        return str(self.list).strip("[]")

    def __lt__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            if summa_self < summa_other:
                return summa_self < summa_other
            if summa_other < summa_self:
                return summa_other < summa_self
        if isinstance(other, list):
            summa_other = sum(other)
            if summa_self < summa_other:
                return summa_self < summa_other
            if summa_other < summa_self:
                return summa_other < summa_self

    def __le__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            if summa_self <= summa_other:
                return summa_self <= summa_other
            if summa_other <= summa_self:
                return summa_other <= summa_self
        if isinstance(other, list):
            summa_other = sum(other)
            if summa_self <= summa_other:
                return summa_self <= summa_other
            if summa_other <= summa_self:
                return summa_other <= summa_self

    def __eq__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            return summa_self == summa_other
        if isinstance(other, list):
            summa_other = sum(other)
            return summa_self == summa_other

    def __ne__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            return summa_self != summa_other
        if isinstance(other, list):
            summa_other = sum(other)
            return summa_self != summa_other

    def __gt__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            if summa_self > summa_other:
                return summa_self > summa_other
            if summa_other > summa_self:
                return summa_other > summa_self
        if isinstance(other, list):
            summa_other = sum(other)
            if summa_self > summa_other:
                return summa_self > summa_other
            if summa_other > summa_self:
                return summa_other > summa_self

    def __ge__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            if summa_self >= summa_other:
                return summa_self >= summa_other
            if summa_other >= summa_self:
                return summa_other >= summa_self
        if isinstance(other, list):
            summa_other = sum(other)
            if summa_self >= summa_other:
                return summa_self >= summa_other
            if summa_other >= summa_self:
                return summa_other >= summa_self

    def __add__(self, other):
        self_lst = []
        for i in self.list:
            if isinstance(i, float):
                i = round(i, 3)
                self_lst.append(i)
            elif isinstance(i, int):
                self_lst.append(i)
            else:
                return f"Your lists are made of wrong type elements"
        if isinstance(other, CustomList):
            other_lst = []
            for i in other.list:
                if isinstance(i, float):
                    i = round(i, 3)
                    other_lst.append(i)
                elif isinstance(i, int):
                    other_lst.append(i)
                else:
                    return f"Your lists are made of wrong type elements"
            if len(self_lst) > len(other_lst):
                dif1 = abs(len(self_lst) - len(other_lst))
                for i in range(dif1):
                    other_lst.append(0)
            else:
                dif2 = abs(len(self_lst) - len(other_lst))
                for i in range(dif2):
                    self_lst.append(0)
            res = [round(el1 + el2, 2) for el1, el2 in zip(self_lst, other_lst)]
            res = CustomList(res)
            return res
        if isinstance(other, list):
            other_lst = []
            for i in other:
                if isinstance(i, float):
                    i = round(i, 3)
                    other_lst.append(i)
                elif isinstance(i, int):
                    other_lst.append(i)
                else:
                    return f"Your lists are made of wrong type elements"
            if len(self_lst) > len(other_lst):
                dif1 = abs(len(self_lst) - len(other_lst))
                for i in range(dif1):
                    other_lst.append(0)
            else:
                dif2 = abs(len(self_lst) - len(other_lst))
                for i in range(dif2):
                    self_lst.append(0)
            res = [round(el1 + el2, 2) for el1, el2 in zip(self_lst, other_lst)]
            res = CustomList(res)
            return res

    def __sub__(self, other):
        self_lst = []
        for i in self.list:
            if isinstance(i, float):
                i = round(i, 2)
                self_lst.append(i)
            elif isinstance(i, int):
                self_lst.append(i)
            else:
                return f"Your lists are made of wrong type elements"
        if isinstance(other, CustomList):
            other_lst = []
            for i in other.list:
                if isinstance(i, float):
                    i = round(i, 2)
                    other_lst.append(i)
                elif isinstance(i, int):
                    other_lst.append(i)
                else:
                    return f"Your lists are made of wrong type elements"
            if len(self_lst) > len(other_lst):
                dif1 = abs(len(self_lst) - len(other_lst))
                for i in range(dif1):
                    other_lst.append(0)
            else:
                dif2 = abs(len(self_lst) - len(other_lst))
                for i in range(dif2):
                    self_lst.append(0)
            res = [round(el1 - el2, 2) for el1, el2 in zip(self_lst, other_lst)]
            res = CustomList(res)
            return res
        if isinstance(other, list):
            other_lst = []
            for i in other:
                if isinstance(i, float):
                    i = round(i, 2)
                    other_lst.append(i)
                elif isinstance(i, int):
                    other_lst.append(i)
                else:
                    return f"Your lists are made of wrong type elements"
            if len(self_lst) > len(other_lst):
                dif1 = abs(len(self_lst) - len(other_lst))
                for i in range(dif1):
                    other_lst.append(0)
            else:
                dif2 = abs(len(self_lst) - len(other_lst))
                for i in range(dif2):
                    self_lst.append(0)
            res = [round(el1 - el2, 2) for el1, el2 in zip(self_lst, other_lst)]
            res = CustomList(res)
            return res


if __name__ == "__main__":
    a = CustomList([1, 2, 3, 4])
    b = CustomList([2, 4, 9, 11, 3])
    c = CustomList([0.2, 0.4, 0.7, 0.4])
    d = CustomList([0.1, 0.3, 0.4])
    e = [2, 3, 5, 8, 9]
    if sum([1, 4, 5]) == sum([1, 2, 3, 4]):
        print("True")

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


    check_instance()
    check_comparison()
    check_sub()
    check_add()
