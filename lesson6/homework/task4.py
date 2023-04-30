# 4.Напишіть функцію change_list, яка приймає список і змінює місця його перший і останній елемент.
# У вихідному списку щонайменше 2 елементи.
def change_list(xlist: []):
    length = len(xlist)
    if length < 2: raise Exception('Length of list <2')
    first, second = xlist[0], xlist[length - 1]
    xlist[0] = second
    xlist[length - 1] = first
