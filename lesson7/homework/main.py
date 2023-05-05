from task1 import change_csv
from task2 import count_files_and_folders

OLD_CSV = 'data/test_file.csv'
NEW_CSV = 'data/salaries_uah.csv'
USD_UAH = 37.54

if __name__ == '__main__':
    # Task-1
    change_csv(OLD_CSV, NEW_CSV, USD_UAH)

    # Task-2
    result = count_files_and_folders(".", 2)
    for k, v in result.items():
        print(k.capitalize(), ' - ',  v)
