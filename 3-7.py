class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        y = 0
        for i in range(len(self.coefficients)):
            y += self.coefficients[i] * (x ** i)
        return y

    def __add__(self, other):
        new_coefficients = []
        len_self = len(self.coefficients)
        len_other = len(other.coefficients)
        max_len = max(len_self, len_other)

        for i in range(max_len):
            if i < len_self and i < len_other:
                new_coefficients.append(self.coefficients[i] + other.coefficients[i])
            elif i < len_self:
                new_coefficients.append(self.coefficients[i])
            else:
                new_coefficients.append(other.coefficients[i])

        return Polynomial(new_coefficients)

poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))