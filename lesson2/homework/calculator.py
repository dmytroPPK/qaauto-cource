print("... Welcome to Calculator !!! ...")
print("Type 2 numbers and  math operation(+,-,*,/)")

while True:
    number_1 = int(input('Number 1: '))
    operation = input('Math operation: ')
    number_2 = int(input('Number 2: '))
    result = None
    if operation == '+':
        result = number_1 + number_2
    if operation == '-':
        result = number_1 - number_2
    if operation == '*':
        result = number_1 * number_2
    if operation == '/':
        result = number_1 / number_2

    print(f'{number_1} {operation} {number_2} = {result}')
    print('Press any key to continue OR Press Q to quit')
    if input().lower() == 'q':
        break
    else:
        continue
