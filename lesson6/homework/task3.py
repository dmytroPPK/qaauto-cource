# 3. Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000, і повертає True,
# якщо це просте число, і False в іншому випадку.
def is_prime(n):
    if n < 2: raise Exception('number < 2')
    if n > 1000: raise Exception('number > 1000')
    if n == 2: return False
    counter = 2
    is_simple = True
    while counter <= n ** 0.5:
        if n % counter == 0:
            is_simple = False
            break
        counter += 1
    return is_simple


if __name__ == '__main__':
    print('-- Test Feature --')
    print(is_prime(3))
    print(is_prime(5))
    print(is_prime(7))
    print(is_prime(11))
