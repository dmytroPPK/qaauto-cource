from math import log, floor

# 1. Дано натуральне число N. Виведіть слово YES, якщо число N є точним ступенем двійки,
# або слово NO інакше. 8 - YES, 3 - NO
def stepin(number):
    stepin = log(number,2)
    return 'YES' if stepin/floor(stepin) == 1. else 'NO'
