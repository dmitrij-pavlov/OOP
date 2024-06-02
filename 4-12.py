class A:
    def __str__(self):
        return "A.str method"

    def hello(self):
        print("Hello")


class B:
    def __str__(self):
        return "B.str method"

    def good_evening(self):
        print("Good evening")


class C(A, B):
    pass


class D(A, B):
    pass


c = C()
c.hello()
c.good_evening()

d = D()
d.hello()
d.good_evening()

print(c)
print(d)