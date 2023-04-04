
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
        return f"{str(self.list).strip('[]')} \n{summa}"

    def __lt__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            return summa_self < summa_other
        if isinstance(other, list):
            summa_other = sum(other)
            return summa_self < summa_other

    def __le__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            return summa_self <= summa_other
        if isinstance(other, list):
            summa_other = sum(other)
            return summa_self <= summa_other

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
            return summa_self > summa_other
        if isinstance(other, list):
            summa_other = sum(other)
            return summa_self > summa_other

    def __ge__(self, other):
        summa_self = sum(self.list)
        if isinstance(other, CustomList):
            summa_other = sum(other)
            return summa_self >= summa_other
        if isinstance(other, list):
            summa_other = sum(other)
            return summa_self >= summa_other

    def __add__(self, other):
        self_lst = []
        for i in self.list:
            self_lst.append(i)
        if isinstance(other, CustomList):
            other_lst = []
            for i in other.list:
                other_lst.append(i)
            if len(self_lst) > len(other_lst):
                dif1 = abs(len(self_lst) - len(other_lst))
                for i in range(dif1):
                    other_lst.append(0)
            else:
                dif2 = abs(len(self_lst) - len(other_lst))
                for i in range(dif2):
                    self_lst.append(0)
            res = [el1 + el2 for el1, el2 in zip(self_lst, other_lst)]
            return res

    def __sub__(self, other):
        self_lst = []
        for i in self.list:
            self_lst.append(i)
        if isinstance(other, CustomList):
            other_lst = []
            for i in other.list:
                other_lst.append(i)
            if len(self_lst) > len(other_lst):
                dif1 = abs(len(self_lst) - len(other_lst))
                for i in range(dif1):
                    other_lst.append(0)
            else:
                dif2 = abs(len(self_lst) - len(other_lst))
                for i in range(dif2):
                    self_lst.append(0)
            res = [el1 - el2 for el1, el2 in zip(self_lst, other_lst)]
            return res


x = 1,2,3
x == 4,5,6
print(x)
