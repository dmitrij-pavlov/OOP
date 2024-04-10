class MinStat:
    def __init__(self):
        self.min_value = None

    def add_number(self, number):
        if self.min_value is None:
            self.min_value = number
        else:
            self.min_value = min(self.min_value, number)

    def result(self):
        return self.min_value


class MaxStat:
    def __init__(self):
        self.max_value = None

    def add_number(self, number):
        if self.max_value is None:
            self.max_value = number
        else:
            self.max_value = max(self.max_value, number)

    def result(self):
        return self.max_value


class AverageStat:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add_number(self, number):
        self.total += number
        self.count += 1

    def result(self):
        if self.count == 0:
            return None
        else:
            return self.total / self.count

values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))