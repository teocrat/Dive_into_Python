class RectangleException(Exception):
    pass


class SideError(RectangleException):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        if self.side1 | self.side2 <= 0:
            return 'Прямоугольник не существует. Сторона меньше или равна нулю.'
