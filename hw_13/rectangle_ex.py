from lesson_13.hw_13.exception_rect import SideError


class Rectangle:
    def __init__(self, len_res, width=None):
        self.len_res = len_res
        self.width = width if width is not None else len_res
        if self.len_res | self.width <= 0:
            raise SideError(self.len_res, self.width)

    def area(self):
        return self.len_res * self.width

    def perimeter(self):
        return (self.len_res + self.width) * 2


if __name__ == '__main__':
    rectangle = Rectangle(12, 2)
    print(rectangle.area())
    print(rectangle.perimeter())
