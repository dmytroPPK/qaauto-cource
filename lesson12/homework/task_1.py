# Використовуючи модуль argparse створити програму розрахунку квадратного рівняння. (Реалізацію самого рівняння
# можете взяти з минулих ДЗ) Запуск програми python main.py -a={} -b={} c={} де параметри
# (a, b, c - параметри квадратного рівняння), за замовчуванням параметр а = 0. При виклику програми з прапорцем --help
# вивести інформацію про програму та про параметри

import argparse

parser = argparse.ArgumentParser(description="Рішення квадратного рівняння з використанням argparse."
                                             " Вкажіть коефіцієти a, b, c")
parser.add_argument("-a", "--a", help="Коефіцієнт a", type=float, default=0)
parser.add_argument("-b", "--b", help="Коефіцієнт b", type=float)
parser.add_argument("-c", "--c", help="Коефіцієнт c", type=float)
args = parser.parse_args()

if args.a == 0:
    print("Коефіцієнт a не може дорівнювати нулю")
    exit()

d = args.b ** 2 - 4 * args.a * args.c
if d < 0:
    print("Рівняння не має дійсних коренів")

elif d == 0:
    x = -args.b / (2 * args.a)
    print(f"Рівняння має один дійсний корінь: x = {x}")

else:
    x1 = (-args.b + d ** 0.5) / (2 * args.a)
    x2 = (-args.b - d ** 0.5) / (2 * args.a)
    print("Рівняння має два дійсних кореня:",
          f"x1 = {x1}",
          f"x2 = {x2}",
          sep='\n')
