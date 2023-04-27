#2. Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c), якщо дискримінант від'ємний
# викликати виняток DiscriminantError і вивести відповідне повідомлення.
def task_2():
    while True:
        try:
            user_input = input("Enter a, b, c separated by spaces: ").split()
            if len(user_input) < 3: raise Exception("less than 3 variables were typed")
            variables = list(map(lambda x: float(x), user_input))
            a, b, c, *carbage = variables
            discriminant = b ** 2 - 4 * a * c
            if discriminant < 0: raise DiscriminantError("Oops... discriminant < 0")
            x1 = (-b + discriminant ** 0.5) / 2 * a
            x2 = (-b - discriminant ** 0.5) / 2 * a
            print(f"x1 = {x1:.5f}, x2 = {x2:.5f}")
            break

        except DiscriminantError as d_err:
            print(d_err)
            break
        except KeyboardInterrupt:
            print(f"\nKeyboardInterrupt exception was occured\nTry again")
            continue
        except Exception as ex:
            print(f'\n<< Wrong input: {ex} >>')
            print("Try again")
            continue

    print("The End of task #2")

class DiscriminantError(Exception):
    pass
class CountOfNumbers(Exception):
    pass


