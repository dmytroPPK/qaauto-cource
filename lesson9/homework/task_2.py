# Знайти найуспішнішого менеджера за підсумковою сумою продажів. Як відповідь потрібно через пробыл
# вказати спершу його ім'я, потім прізвище і після загальну суму його продажів.Файл manager_sales.json

import json


def find_best_manager(rel_path: str) -> [dict]:

    with open(rel_path) as file:
        json_result = json.load(file)

    dict_helper = dict()

    for item in json_result:
        f_name = item['manager']['first_name']
        l_name = item['manager']['last_name']
        key_of_dict = (f_name, l_name)
        sum_all_prices = 0
        for inner_dict in item['cars']:
            sum_all_prices += inner_dict['price']
        dict_helper[key_of_dict] = sum_all_prices

    max_sales = max(list(dict_helper.values()))
    result_list = []

    for k, v in dict_helper.items():
        if v == max_sales:
            manager = dict(f_name=k[0], l_name=k[1], summa=v)
            result_list.append(manager)

    return result_list
