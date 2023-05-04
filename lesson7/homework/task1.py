# Открыть файл test_file.csv, прочитать, распарсить зп сотрудников в долларах и перевести в гривны на текущую
# дату(курс задается отдельной переменной). Результат сохранить в новый файл salaries_uah.csv
import os


def change_csv(file_name: str, new_file_name: str, rate: float):
    file_path = os.path.join(os.getcwd(), file_name)
    if not os.path.isfile(file_path):
        raise Exception("FIle not found ...")
    with open(file_path, "r+") as file1:
        list_of_file = file1.readlines()
        with open(new_file_name, 'a+') as file2:
            for index, value in enumerate(list_of_file):
                if index == 0:
                    file2.write(value)
                    continue
                line_as_list = [float(v) * rate if i != 0 else v for i, v in enumerate(value.split(','))]
                line_to_write = f"{','.join(map(str, line_as_list))}\n"
                file2.write(line_to_write)
