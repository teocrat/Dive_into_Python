from math import pi


class Circle:
    """

    >>> Circle(3).len_circle()
    18.84955592153876
    >>> Circle(3).square()
    28.274333882308138

    """

    def __init__(self, rad):
        self.rad = rad

    def len_circle(self):
        return 2 * pi * self.rad

    def square(self):
        return pi * self.rad ** 2


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
