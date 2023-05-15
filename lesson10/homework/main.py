from decorators import tictac, logging


@tictac
def summa_one(*args):
    return sum(args)


@logging
def summa_two(*args):
    return sum(args)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = summa_one(*data)
    print(result)

    data = [1, 2, 3, 4, 5, 6, 7, 8, 7, 5, 15]
    result = summa_two(*data)
    print(result)
