# 4.Напишіть функцію change_list, яка приймає список і змінює місця його перший і останній елемент.
# У вихідному списку щонайменше 2 елементи.
def change_list(xlist: []):
    if len(xlist) < 2:
        raise Exception('Length of list < 2')
    xlist[0], xlist[-1] = xlist[-1], xlist[0]
