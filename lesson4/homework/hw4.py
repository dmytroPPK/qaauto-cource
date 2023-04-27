# Існує список з іменами ["john", "marta", "james", "amanda", "marianna"], перетворити рядок,
# щоб кожне ім'я явно починалися з великої літери.
def task_1():
    names = ["john", "marta", "james", "amanda", "marianna"]
    names = [item.title() for item in names]
    for i in names:
        print(i)


# Є список друзів ["John", "Marta", "James", "Amanda", "Marianna"]. Виведіть імена в консолі, кожен з нового рядка,
# вирівнюючи праву сторону, використовуючи метод рядка та форматування через F String. Також над іменами першим рядком
# виведіть NAME, де NAME має бути посередині(string.center()), а решта простору заповнена символом "*"
def task_2():
    friends = ["John", "Marta", "James", "Amanda", "Marianna"]
    max_name_length = 0
    for i in friends:
        if max_name_length < len(i): max_name_length = len(i)
    result = f"{'NAME'.center(max_name_length, '*')}\n"
    for i in friends:
        result += f"{i:>{max_name_length}}\n"
    print(result)


# У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] , перетворити його у список
# змінних для Пайтона snace_case, "friends_list", "my_tuple"]
def task_3():
    variables = ["FirstItem", "FriendsList", "MyTuple"]
    for index, value in enumerate(variables):
        new_variable_as_list = []
        for index_char, char in enumerate(value):
            if index_char == 0:
                new_variable_as_list.append(char.lower())
            elif char.isupper() and index_char != 0:
                new_variable_as_list.append(f"_{char.lower()}")
            else:
                new_variable_as_list.append(char)
        variables[index] = ''.join(new_variable_as_list)
    print(variables)


# Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
# Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python.
# It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника.
# Виведіть словник на екран.
def task_4():
    data_dict = {"Python": "Guido van Rossum",
                 "Java": "Oracle Corporation",
                 "C#": "Anders Hejlsberg",
                 "JS": "Brendan Eich"}
    for k, v in data_dict.items():
        print(f"My favorite programming language is {k}.\n  It was created by {v}.")
    del data_dict["Python"]
    print("\n--- List after item was deleted ---")
    for k, v in data_dict.items():
        print(k, '-', v)


# Створіть англо-німецький словник, який називається e2g, і виведіть його на екран. Слова для словника:
# stork / storch, hawk / falke, woodpecker / specht і owl / eule. Виведіть німецький варіант слова owl.
# Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
# Виведіть окремо: словник; ключі і значення словника у вигляді списків.
def task_5():
    e2g_dict = dict(stork='storch', hawk='falke', woodpecker='specht', owl='eule')
    show_data = "owl"
    print(f"{show_data} in German is {e2g_dict[show_data]}")
    e2g_dict["nightingale"] = "nachtigall"
    e2g_dict["pigeon"] = "taube"

    print("\n -- New Dict --")
    for k, v in e2g_dict.items():
        print(k, '-->', v)

    print("\n-- Keys and Values lists --")
    keys_as_list = list(e2g_dict.keys())
    print(f"List of keys: {keys_as_list}")

    values_as_list = list(e2g_dict.values())
    print(f"List of values: {values_as_list}")


#Створіть багаторівневий словник subjects навчальних предметів. Використайте наступні рядки для ключів
# верхнього рівня: 'science', 'humanities' і 'public'. Зробіть так, щоб ключ 'science' був ім’ям іншого словника,
# який має ключі 'physics', 'computer science' і 'biology'. Зробіть так, щоб ключ 'physics' посилався на список
# рядків зі значеннями 'nuclear physics', 'optics' і 'thermodynamics'. Решта ключів повинні посилатися на порожні
# словники. Виведіть на екран ключі subjects['science'] і значення subjects['science']['physics'].
def task_6():
    subjects = {
        "science":{
            "physics":[
                "nuclear physics",
                "optics",
                "thermodynamics"
            ],
            "computer science":{},
            "biology":{}
        },
        "humanities":{},
        "public":{}
    }
    print(f'Keys of subjects["science"] are {list(subjects["science"].keys())}')
    print(f'Value of subjects["science"]["physics"] is {subjects["science"]["physics"]}')



# Напишіть програму, яка виводить словник, в якому ключі є числами від 1 до 15 (обидва включені),
# а значення є квадратами ключів. Генерація ключів та значень має бути виконана через цикл.
def task_7():
    start, end = 1, 15
    result_dict = dict()
    for i in range(start, end + 1):
        result_dict[str(i)] = i ** 2

    print(result_dict)


# Run tasks
# task_1()
# task_2()
# task_3()
# task_4()
# task_5()
# task_6()
# task_7()
