#2. Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення
# (за допомогою кортежу): периметр квадрата, площа квадрата та діагональ квадрата.
def square(length):
    perimetr = 4 * length
    plosha = length ** 2
    diagonal = (length ** 2 + length ** 2) ** 0.5
    return perimetr, plosha, diagonal
