# 5. Напишіть функцію to_dict(lst), яка приймає аргумент у вигляді списку і повертає словник, в якому кожен
# елемент списку є ключем і значенням. Передбачається, що елементи списку відповідатимуть правилам
# завдання ключів у словниках.
def to_dict(xlist: []):
    if not xlist:
        raise Exception('Empty list was detected ...')
    result_dict = dict()
    for item in xlist:
        result_dict[item] = item
    return result_dict
