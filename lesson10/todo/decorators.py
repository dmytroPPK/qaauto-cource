import datetime
#
# def cat():
#     print('Meo')
#
#
# cat()
#
#
# def cat():
#     def say():
#         return 'Meo'
#     return say()
#
#
# print(cat())
#
#
# def say_something():
#     return 'Glory Ukraine'
#
#
# def say_after_function(func):
#     print(func)
#     print('Do something')
#
#
# say_after_function(say_something)


# def animal(type_animal='cat'):
#     def cat():
#         return "Meo"
#
#     def dog():
#         return 'Wood'
#
#     if type_animal == "cat":
#         return cat
#     else:
#         return dog
#
# print(animal()())
#
# def cat():
#     print('Meo')
import time


# def my_decorator(func):
#     def my_wrapper():
#         start = datetime.datetime.now()
#         func()
#         finish = datetime.datetime.now()
#         delta = finish - start
#         print(f'Time for {func} {delta}')
#     return my_wrapper
#
#
# @my_decorator
# def dog():
#     time.sleep(2)
#     print('Woof !')
#
#
# dog()


# def my_decorator(func):
#     def my_wrapper(arg1, arg2):
#         print(f'I get {arg1} and {arg2}')
#         func(arg1, arg2)
#     return my_wrapper
#
# @my_decorator
# def full_name(first_name, last_name):
#     print(f"My full name {first_name} {last_name}")
#
# full_name('Joe','Koen')

#
def my_decorator(ukraine_glory):
    def my_wrapper(*args, **kwargs):
        print(f'I get args - {args}')
        print(f'I get kwargs - {kwargs}')
        ukraine_glory(*args, **kwargs)
    return my_wrapper


@my_decorator
def my_func(*args, **kwargs):
    for _ in args:
        print(_)
    print(f'Our kwargs {kwargs}')
    print('Python is cool')


kwargs_param = {'q': 2, 'p': 4}
args_param = (1, 22, 3, 4)

my_func(*args_param, **kwargs_param)

# def summ(*args):
#     print(args)
#     print(sum((args)))
#
# summ(1, 2, 3, 4, 33, 43, 53, 43, 23)