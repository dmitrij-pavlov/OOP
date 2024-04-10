class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, other):
        x = max(self.x, other.get_x())
        y = max(self.y, other.get_y())
        w = min(self.x + self.w, other.get_x() + other.get_w()) - x
        h = min(self.y + self.h, other.get_y() + other.get_h()) - y

        if w < 0 or h < 0:
            return None

        return Rectangle(x, y, w, h)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(5, 5, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())