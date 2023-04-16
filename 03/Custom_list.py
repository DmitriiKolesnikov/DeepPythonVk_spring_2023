class CustomList(list):

    def __init__(self, data):
        super(CustomList, self).__init__()
        self.list = []
        if data:
            self.list = list(data)

    def __str__(self):
        summa = 0
        self_lst = []
        for i in self.list:
            if type(i) == int:
                summa += i
            elif type(i) == float:
                summa += round(i, 3)
            else:
                return f"Unexpected type of data. Check your CustomList"
        summa = str(round(summa, 2))
        res_sum = "Summa = " + summa
        for i in self.list:
            self_lst.append(i)
        self_lst.append(res_sum)
        return self_lst

    def __eq__(self, other):
        i = 0
        if isinstance(i, (int, float)):
            pass
        else:
            print("Wrong type of i")
        summa1 = sum(self.list)
        if isinstance(other, CustomList):
            for i in other.list:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other.list)
            return summa1 == summa2
        if isinstance(other, list):
            for i in other:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other)
            return summa1 == summa2

    def __ne__(self, other):
        i = 0
        if isinstance(i, (int, float)):
            pass
        else:
            print("Wrong type of i")
        summa1 = sum(self.list)
        if isinstance(other, CustomList):
            for i in other.list:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other.list)
            return summa1 != summa2
        if isinstance(other, list):
            for i in other:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other)
            return summa1 != summa2

    def __lt__(self, other):
        i = 0
        for i in self.list:
            if isinstance(i, (int, float)):
                pass
            else:
                print("Wrong type of i")
        summa1 = sum(self.list)
        if isinstance(other, CustomList):
            for i in other.list:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other.list)
            return summa1 < summa2
        if isinstance(other, list):
            for i in other:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other)
            return summa1 < summa2

    def __le__(self, other):
        i = 0
        if isinstance(i, (int, float)):
            pass
        else:
            print("Wrong type of i")
        summa1 = sum(self.list)
        if isinstance(other, CustomList):
            for i in other.list:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other.list)
            return summa1 <= summa2
        if isinstance(other, list):
            for i in other:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other)
            return summa1 <= summa2

    def __gt__(self, other):
        i = 0
        if isinstance(i, (int, float)):
            pass
        else:
            print("Wrong type of i")
        summa1 = sum(self.list)
        if isinstance(other, CustomList):
            for i in other.list:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other.list)
            return summa1 > summa2
        if isinstance(other, list):
            for i in other:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other)
            return summa1 > summa2

    def __ge__(self, other):
        i = 0
        if isinstance(i, (int, float)):
            pass
        else:
            print("Wrong type of i")
        summa1 = sum(self.list)
        if isinstance(other, CustomList):
            for i in other.list:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other.list)
            return summa1 >= summa2
        if isinstance(other, list):
            for i in other:
                if isinstance(i, (int, float)):
                    pass
                else:
                    print("Wrong type of i")
            summa2 = sum(other)
            return summa1 >= summa2

    def __add__(self, other):
        self_lst = []
        for i in self.list:
            if isinstance(i, (int, float)):
                self_lst.append(i)
            else:
                return f"Your lists are made of wrong type elements"
        if isinstance(other, CustomList):
            other_lst = []
            for i in other.list:
                if isinstance(i, (int, float)):
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
            res = CustomList([round(el1 + el2, 2) for el1, el2 in zip(other_lst, self_lst)])
            return res
        if isinstance(other, list):
            other_lst = []
            for i in other:
                if isinstance(i, (int, float)):
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
            res = CustomList([round(el1 + el2, 2) for el1, el2 in zip(self_lst, other_lst)])
            return res

    def __sub__(self, other):
        if self.list is None:
            print(None)
        self_lst = []
        for i in self.list:
            if isinstance(i, (int, float)):
                self_lst.append(i)
            else:
                return f"Your lists are made of wrong type elements"
        if isinstance(other, CustomList):
            other_lst = []
            for i in other.list:
                if isinstance(i, (int, float)):
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
            res = CustomList([round(el1 - el2, 2) for el1, el2 in zip(self_lst, other_lst)])
            return res
        if isinstance(other, list):
            other_lst = []
            for i in other:
                if isinstance(i, (int, float)):
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
            res = CustomList([round(el1 - el2, 2) for el1, el2 in zip(self_lst, other_lst)])
            return res

