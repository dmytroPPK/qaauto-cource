from task1 import stepin
from task2 import square
from task3 import is_prime
from task4 import change_list
from task5 import to_dict
from task6 import sum_range

FILL_WIDTH = 50
FILL_CHAR = '-'

if __name__ == "__main__":
    # Task-1
    print(" Task-1 ".center(FILL_WIDTH, FILL_CHAR))

    number1, number2 = 3, 8
    print(f"{number1} є точним ступенем 2 ? - {stepin(number1)}")
    print(f"{number2} є точним ступенем 2 ? - {stepin(number2)}")

    # Task-2
    print(" Task-2 ".center(FILL_WIDTH, FILL_CHAR))

    storona = 1
    result = square(storona)
    print(f"Квадрат зі стороною {storona} має:\n периметр - {result[0]}\n "
          f"площу - {result[1]}\n діагональ - {result[2]:.5f} ")

    # Task-3
    print(" Task-3 ".center(FILL_WIDTH, FILL_CHAR))

    print(f"2 is prime - {is_prime(2)}")
    print(f"3 is prime - {is_prime(3)}")
    print(f"9 is prime - {is_prime(9)}")
    print(f"5 is prime - {is_prime(5)}")
    print(f"25 is prime - {is_prime(25)}")

    # Task-4
    print(" Task-4 ".center(FILL_WIDTH, FILL_CHAR))

    our_list = ['last', 1, 2, 3, 'first']
    print(f"Init list\n - {our_list}")
    change_list(our_list)
    print(f"Changed list\n - {our_list}")

    # Task-5
    print(" Task-5 ".center(FILL_WIDTH, FILL_CHAR))

    inti_list = [1, 2, True, False, 'Hello']
    result_dict = to_dict(inti_list)
    print(f"List: {inti_list}")
    print(f"Dict: {result_dict}")

    # Task-6
    print(" Task-6 ".center(FILL_WIDTH, FILL_CHAR))

    sum_case1 = sum_range(1, 5)
    print(f"sum_range(1, 5) = {sum_case1}")
    sum_case2 = sum_range(5, 4)
    print(f"sum_range(5, 4) = {sum_case2}")
