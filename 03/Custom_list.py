
  class CustomList(list):

    def __add__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
            result_len = max(len(self), len(other))
            return CustomList([self[i] + other[i] if i < len(self) and i < len(other) else (self[i] if i < len(self)
                                                                                            else other[i]) for i in
                               range(result_len)])

    def __sub__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
        result_len = max(len(self), len(other))
        return CustomList([self[i] - other[i] if i < len(self) and i < len(other) else (self[i] if i < len(self) else
                                                                                        -other[i]) for i in
                           range(result_len)])

    def __eq__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
        return sum(self) == sum(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
        return sum(self) > sum(other)

    def __ge__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
        return sum(self) >= sum(other)

    def __lt__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
        return sum(self) < sum(other)

    def __le__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
        return sum(self) <= sum(other)

    def __str__(self):
        return f'{super().__str__()} sum={sum(self)}'
