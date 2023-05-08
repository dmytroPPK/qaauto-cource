#1. Написать свой тип данных для сложения и вычитания, сравнение комплексных чисел. А так же правильного
# отображение их в консоли(magic method __str__).

class MyComplex:
    def __init__(self, real = 0, imagine = 0):
        if type(real) not in (int,float) or type(imagine) not in (int,float):
            raise ValueError("Both parts must be a number")
        self.__real = real
        self.__imagine = imagine

    @property
    def real(self):
        return self.__real

    @property
    def imagine(self):
        return self.__imagine

    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        sign = '+' if self.__imagine >= 0 else ''
        return f"{self.__real}{sign}{self.__imagine}i"
    def __add__(self, obj2:'MyComplex'):
        return MyComplex(self.__real + obj2.real, self.__imagine + obj2.imagine)
    def __sub__(self, obj2:'MyComplex'):
        return MyComplex(self.__real - obj2.real, self.__imagine - obj2.imagine)

    def __eq__(self, obj2:'MyComplex'):
        return self.__real == obj2.real and self.__imagine == obj2.imagine
    def __ne__(self, obj2:'MyComplex'):
        return not self.__eq__(obj2)

    def __lt__(self, obj2:'MyComplex'):
        return (self.__real < obj2.real)  or ( self.__real == obj2.real and self.__imagine < obj2.imagine)

    def __le__(self, obj2:'MyComplex'):
        return (self.__real <= obj2.real)  and ( self.__imagine <= obj2.imagine)

    def __gt__(self, obj2:'MyComplex'):
        return (self.__real > obj2.real) or ( self.__real == obj2.real and self.__imagine > obj2.imagine)

    def __ge__(self, obj2:'MyComplex'):
        return (self.__real >= obj2.real)  and ( self.__imagine >= obj2.imagine)

