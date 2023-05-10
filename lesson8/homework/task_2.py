#2. Написать класс для сущности Точка(содержит в себе координаты Х и Y). Написать классы для сущностей Треугольник,
# Квадрат, которые аггрегируют объекты класса Точка. Написать методы, которые считают площадь фигур, если
# координаты введены правильно. Если нет, то показать сообщение об ошибке.

class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(x, (int, float)):
            raise ValueError("x,y must be int or float")
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

class Triangle:
    def __init__(self, p1:'Point', p2:'Point', p3:'Point'):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    @classmethod
    def validate_coordinates(cls, p1:'Point', p2:'Point', p3:'Point'):
        if (p1.x == p2.x and p1.y == p2.y) or (p2.x == p3.x and p2.y == p3.y) or (p3.x == p1.x and p3.y == p1.y):
            return False
        return True

    def calc_area(self):
        if not self.validate_coordinates(self._p1, self._p2, self._p3):
            raise ValueError("Figure has invalid coordinates")
        a = ( (self._p2.x - self._p1.x) ** 2 + (self._p2.y - self._p1.y) ** 2 ) ** 0.5
        b = ( (self._p3.x - self._p2.x) ** 2 + (self._p3.y - self._p2.y) ** 2 ) ** 0.5
        c = ( (self._p1.x - self._p3.x) ** 2 + (self._p1.y - self._p3.y) ** 2 ) ** 0.5

        p = ( a + b + c ) / 2
        s = ( p * (p - a) * (p - b) * (p - c) ) ** 0.5
        return s


class Square:
    def __init__(self, p1:'Point', p2:'Point', p3:'Point', p4:'Point'):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._p4 = p4

    @classmethod
    def validate(cls, p1:'Point', p2:'Point', p3:'Point', p4:'Point'):
        a = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
        b = (p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2
        c = (p3.x - p4.x) ** 2 + (p3.y - p4.y) ** 2
        d = (p4.x - p1.x) ** 2 + (p4.y - p1.y) ** 2
        if not (a == b == c == d):
            return False
        return True


    def calc_area(self):
        if not self.validate(self._p1, self._p2, self._p3, self._p4):
            raise ValueError("Square doesn't have all equal sides.")
        side = ( (self._p1.x - self._p2.x) ** 2 + (self._p1.y - self._p2.y) ** 2 ) ** 0.5
        square = side ** 2
        return square


if __name__ == '__main__':
    p1 = Point(3.5,4)
    p2 = Point(5,1.5)
    p3 = Point(2,2)

    triangle = Triangle(p1,p2,p3)
    s = triangle.calc_area()
    print(s)

    p1 = Point(1,1)
    p2 = Point(3,1)
    p3 = Point(3, 3)
    p4 = Point(1, 3)

    square = Square(p1, p2, p3, p4)
    s = square.calc_area()
    print(s)


