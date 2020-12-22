""" Exercise 6
        Реализовать два небольших скрипта:
        а) итератор, генерирующий целые числа, начиная с указанного,
        б) итератор, повторяющий элементы некоторого списка, определенного заранее.

        Подсказка: использовать функцию count() и cycle() модуля itertools.
        Обратите внимание, что создаваемый цикл не должен быть бесконечным.
        Необходимо предусмотреть условие его завершения.
        Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
        Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

        ПРИМЕЧАНИЕ ОТ РАЗРАБОТЧИКА:
            2 аргументом скрипту передавать int - начальное значение для count()
            3 аргументом скрипту передавать str - данные для cycle()
"""
from sys import argv
from itertools import (
                        count,
                        cycle
                       )

def check_inp(data: str, numb: int) -> int:
    """
        Функция пытается поменять тип данных с str на int. Если не получается - завершает работу программы
        и выдаёт ошибку.
        :param data: str
        :param numb: int
        :return: int
    """
    try:
        return int(data)
    except ValueError:
        exit(f"Ошибка! {numb + 1} аргумент должен быть числом!")


if len(argv) != 3:
    exit("Ошибка! Введено неверное количество аргументов!")
else:
    data_count = check_inp(argv[1], 1)
    data_cycle = argv[2]

    count_list = []
    for element in count(data_count):
        if element > data_count + 10:
            break
        else:
            count_list.append(element)

    cycle_list = []
    count = 0
    for element in cycle(data_cycle):
        if count < 10:
            cycle_list.append(element)
            count += 1
        else:
            break

    print(f"count_list = {count_list}")
    print(f"cycle_list = {cycle_list}")

