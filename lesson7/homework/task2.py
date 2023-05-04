# Написать скрипт, который подсчитает количество папок и файлов по заданному пути. Если такого нет, то по всей
# системе(/ - для линукс/мак. Диск С - для виндоус). Для удобства можно установить граничное значение числа
# папок(и/или файлов), после которого скрипт не будет продолжать работу. Среди найденных файлов показать самый
# большой и самый маленький по размеру, а так же с самым длинным и коротким именем. Если во время работы скрипт
# был прерван(KeyboardInterrupt), то промежуточные результаты сериализуются в файл и при повторном запуске эти
# пути исключаются из проверки.

import os
import json

DUMPS_DIR = 'dump'
DUMPS_FILE = 'dump1.txt'


def count_files_and_folders(path: str, depth: int = 1):
    exp_dict = dict(paths=[], files=[], dirs=[])
    json_dict: dict = {}
    file_path = os.path.join(DUMPS_DIR, DUMPS_FILE)
    try:
        if not os.path.exists(path):
            path = '/'
        if depth < 0:
            depth = 1

        count = 0
        cwd = os.getcwd()

        if os.path.isfile(file_path):
            json_dict = dict_from_file(file_path)
        for rpath, dirs, files in os.walk(path):
            if count == depth:
                break
            if bool(json_dict) and rpath in json_dict['paths']:
                count += 1
                continue
            exp_dict['paths'].append(rpath)
            for item in files:
                exp_dict['files'].append(os.path.join(cwd, rpath, item))
            for item in dirs:
                exp_dict['dirs'].append(item)
            count += 1

        if json_dict is not None:
            exp_dict['files'].extend(json_dict['files'])
            exp_dict['dirs'].extend(json_dict['dirs'])
    except KeyboardInterrupt:
        print("KeyboardInterrupt exception is raised. ")
        dict_to_file(exp_dict, file_path)
        print(f"Intermediate results were dumped into file:\n{os.path.abspath(os.path.join(DUMPS_DIR, DUMPS_FILE))}")
    return get_file_info(exp_dict)


def get_file_info(source_dict: dict):
    name_size = {}
    for file_path in source_dict['files']:

        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            name_size[file_size] = os.path.abspath(file_path)
        else:
            raise Exception(f'Cannot check file size - {file_path}')

    names_by_path = list(name_size.values())
    name_of_files = [i.split('/')[-1] for i in names_by_path]
    path_to_length = {}
    for k, v in zip(names_by_path, name_of_files):
        path_to_length[k] = len(v)

    max_length_name = []
    min_length_name = []
    max_length = max(list(path_to_length.values()))
    min_length = min(list(path_to_length.values()))
    for k, v in path_to_length.items():
        if max_length == v:
            max_length_name.append(k)
        if min_length == v:
            min_length_name.append(k)

    max_size = max(list(name_size.keys()))
    max_size_name = name_size[max_size]
    min_size = min(list(name_size.keys()))
    min_size_name = name_size[min_size]
    count_files = len(source_dict['files'])
    count_dirs = len(source_dict['dirs'])
    return dict(
        count_of_files=count_files,
        count_of_dirs=count_dirs,
        biggest_file=f"{max_size} bytes of {max_size_name}",
        smallest_file=f"{min_size} bytes of {min_size_name}",
        min_length_files=f"{min_length} symbols have files:\n{chr(0x0A).join(min_length_name)}",
        max_length_files=f"{max_length} symbols have files :\n{chr(0x0A).join(max_length_name)}"
    )


def dict_to_file(value: dict, file_path):
    dict_as_string = json.dumps(value)
    if not os.path.exists(DUMPS_DIR):
        os.mkdir(DUMPS_DIR)
    with open(file_path, 'w+') as file:
        file.write(dict_as_string)


def dict_from_file(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
        return json.loads(content)


__all__ = ['count_files_and_folders']
