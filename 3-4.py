class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0
        days += self.day - other.day
        for i in range(other.month, self.month):
            days += days_in_month[i]
        return days

jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)  # Output: 4
print(jan1 - jan5)  # Output: -4
print(jan1 - jan1)  # Output: 0
print(jan5 - jan5)  # Output: 0