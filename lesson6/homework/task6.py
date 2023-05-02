# 6.Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до
# величини end включно. Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.
def sum_range(start, end):
    if start > end:
        start, end = end, start
    list_to_sum = list(range(start, end + 1))
    return sum(list_to_sum)
