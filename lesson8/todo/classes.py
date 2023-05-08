class A:
    class_attribute = 0

    def __new__(cls):
        print(f'Creating a new {cls.__name__} object...')
        return super().__new__(cls)

    def __init__(self):
        print('Initialize object variables')

    @staticmethod
    def static_method():
        print('Static method without self')

    @classmethod
    def class_method(cls):
        print('Class method without object')


if __name__ == '__main__':
    a = A()
    a.static_method()
    A.static_method()
    A.class_method()
