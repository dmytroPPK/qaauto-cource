# Знайти ідентифікатор групи, де знаходиться найбільша кількість жінок, народжених після 1977 року.
# Як відповідь необхідно вказати через пробыл ідентифікатор знайденої групи і скільки в ній було жінок,
# народжених після 1977 року. Файл group_people.json
import json


def find_max_people(rel_path: str) -> [tuple]:

    with open(rel_path) as file:
        json_result = json.load(file)

    dict_helper = dict()

    for item in json_result:
        key_of_dict = f"id-{item['id_group']}"
        cnt_found_people = 0
        for inner_dict in item['people']:
            if inner_dict['year'] > 1977 and inner_dict['gender'] == 'Female':
                cnt_found_people += 1
        dict_helper[key_of_dict] = cnt_found_people

    max_cnt = max(list(dict_helper.values()))
    result_list = []

    for k, v in dict_helper.items():
        if v == max_cnt:
            result_list.append((k[3:], v))

    return result_list
