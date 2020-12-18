""" Exercise 1
        Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
        В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
        Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

name_list = ["work_time", "time_rate", "prize"]
arg_count = 0
my_dict = {}

if len(argv) != 4:
    exit("Ошибка! Введено неверное количество аргументов!")
else:
    for element in argv[1:]:
        try:
            my_dict[name_list[arg_count]] = float(argv[arg_count + 1])
            arg_count += 1
        except ValueError:
            exit(f"Ошибка! {arg_count + 1} аргумент должен быть числом!")

wage = my_dict[name_list[0]] * my_dict[name_list[1]] + my_dict[name_list[2]]
print(wage)
