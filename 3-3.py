class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c


sf = SquareFunction(2, 3, 5)
print(sf(2))  
print(sf(-1)) 
