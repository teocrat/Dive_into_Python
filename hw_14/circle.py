from math import pi


class Circle:
    def __init__(self, rad):
        self.rad = rad

    def len_circle(self):
        return 2 * pi * self.rad

    def square(self):
        return pi * self.rad ** 2


if __name__ == '__main__':
    c = Circle(3)
    print(c.len_circle())
    print(c.square())
