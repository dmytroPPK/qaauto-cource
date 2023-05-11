from task_1 import find_max_people
from task_2 import find_best_manager

if __name__ == '__main__':

    # Task-1
    result_1 = find_max_people('data/group_people.json')
    for i in result_1:
        print(f"In group {i[0]} {i[1]} women")

    # Task-2
    result_2 = find_best_manager('data/manager_sales.json')
    for i in result_2:
        print(i['f_name'], i['l_name'], i['summa'])
