from exceptions_lib import *

# 2. Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c), якщо дискримінант від'ємний
# викликати виняток DiscriminantError і вивести відповідне повідомлення.
def task_2():
    print("Start of task #2")
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



# Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа, оператора
# (як мінімум + і -) та іншого числа, розділених пробілом (наприклад, 1 + 1). Використовуйте str.split()

## a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.

## b. Спробуйте перетворити перший і третій елемент на float ( float_value = float(str_value)). Спіймайте будь-яку
## ValueError і згенеруйте замість нього FormulaError

## c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError
def task_3():
    print("Start of task #3")
    while True:
        try:
            user_input = input("Enter number, sign, number separated by spaces: ").split()
            if len(user_input) < 3: raise FormulaError("less than 3 items were typed")
            try:
                input_items = [float(v) if i in (0, 2) else v for i, v in enumerate(user_input)]
                a, sign, b, *carbage = input_items
            except ValueError as v_err:
                raise FormulaError(v_err)
            if (input_items[1] not in "+-*/"):
                raise FormulaError("Invalid sign was typed")
            print(a, sign, b, end=' = ')
            # замість if або match чуточку збочення)
            eval(f"print({a} {sign} {b} )")
            break
        except FormulaError as form_ex:
            print(f" Warning! - {form_ex}\n Try again")
            continue
        except KeyboardInterrupt:
            print(f"\n KeyboardInterrupt exception was occured\n Try again")
            continue
        except Exception:
            print(f'\n<< Oops something went wrong, Bye ) >>')
            exit()
    print("The End of task #3")


