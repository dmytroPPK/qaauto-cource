import time
import datetime


# Створити декоратор який вимірює час виконання функції
def tictac(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        delta = time.time() - start
        print(f"Function '{func.__name__}' took {delta:.10f} seconds")
        return res
    return wrapper

# Створити декоратор який кожен раз буде записувати у файл результат роботи якоїсь функції після її виклику
# (наприклад функція яка прораховує суму всіх переданих аргументів *args). Запис в файл формату ""Function launched
# at {час запуску} with result {результат роботи функції}
def logging(func):
    def wrapper(*args):
        time_now = datetime.datetime.now()
        time_format = time_now.strftime("%H:%M:%S on %dth of %B %Y")
        res = func(*args)
        message = f"Function '{func.__name__}' launched at {time_format} with result {res}\n"
        with open('logs.txt', 'a') as file:
            file.write(message)
        return res
    return wrapper
