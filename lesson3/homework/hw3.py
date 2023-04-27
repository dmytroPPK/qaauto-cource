# Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
def task_1():
    user_input = input("Please type any word: ")
    result = '+' if user_input == user_input[::-1] else '-'
    print(f'Is this word polindrom ? => " {result} "')

# Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті,
# вивести 'YES', інакше 'NO'
def task_2():
    sentence = input("Please type any sentence: ")
    word = input("Please type the word: ")
    result = 'YES' if word in sentence else 'NO'
    print(f'Word is in sentence - {result}')

# Користувач вводить рядок. Якщо він починається на 'abc', замінити їх на 'www',
# інакше додати в кінець рядка 'zzz'
def task_3():
    user_input = input('Please type any phrase: ')
    result = 'www' + user_input[3:] if user_input[:3] == 'abc' else user_input + 'www'
    print(f'Result: {result}')

# Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити,
# що в пошті є символ '@' і '.', і якщо це так, вивести "YES", інакше "NO"
def task_4():
    email = input('Pleae type your email: ')
    output = 'Is email valid - " {} "'
    if '@' not in email or '.' not in email:
        print(output.format('NO'))
    else:
        print(output.format('YES'))

# Користувач вводить текст через пробіл. Конвертувати текст у список. Вивести остані 3 елементи зі списку,
# якщо список містить менше 3-х елементів, вивести повідомлення про те що кількість елементів менша за 3
# і вказати кількість елементів поточного списку
def task_5():
    user_input = input('Please type phrase with spaces: ').strip()
    list_input = user_input.split(' ')
    items_qnt = len(list_input)
    if items_qnt < 3 :
        print(f'{items_qnt} item(s) in the list and there is < 3')
    else:
        print(f"3 last items of list: {list_input[-3:]}")


# Run HomeWork

# task_1()
# task_2()
# task_3()
# task_4()
# task_5()