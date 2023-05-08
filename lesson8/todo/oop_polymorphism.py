class Animal:

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    def say_it(self):
        print('Meow!')


class Dog(Animal):

    def say_it(self):
        print('Auf!')


class Snake(Animal):

    def say_it(self):
        print('Где зарплата?')


if __name__ == '__main__':
    cat = Cat('Redneck')
    dog = Dog('Hillbilly')
    snake = Snake('Tamara')

    for animal in [cat, dog, snake]:
        animal.say_it()
