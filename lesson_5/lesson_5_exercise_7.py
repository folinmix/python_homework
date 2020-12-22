""" Exercise 7
        Создать (не программно) текстовый файл, в котором каждая строка должна содержать
        данные о фирме: название, форма собственности, выручка, издержки.

        Пример строки файла: firm_1 ООО 10000 5000.

        Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
        Если фирма получила убытки, в расчет средней прибыли ее не включать.
        Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
        а также словарь со средней прибылью.
        Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

        Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
        Итоговый список сохранить в виде json-объекта в соответствующий файл.

        Пример json-объекта:
        [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

        Подсказка: использовать менеджеры контекста.
"""
import json

full_list = []
firm_dict = {}
average_dict = {}
average_name = 'average_profit'
average_profit = 0
count = 1
line_number = 1


def int_check(data: str, line_num: int) -> int:
    """
        Функция пытается преобразовать str в int. Если не получается - возвращается ошибка
        :param data: str
        :param line_num: int
        :return: int
    """
    try:
        return int(data)
    except ValueError:
        print(f"Ошибка! В {line_num} строке введены недопустимые символы!")


with open("txt_files/exercise_7/program_in.txt", 'r', encoding='UTF-8') as file:
    data_file = file.readlines()
    for line in data_file:
        *name_list, form, profit, costs = line.split()
        company_name = ' '.join(name_list)
        profit = int_check(profit, line_number)
        costs = int_check(costs, line_number)

        profit_difference = profit - costs

        firm_dict[(form + ' ' + company_name)] = profit_difference
        if profit_difference >= 0:
            average_profit += profit_difference
            count += 1
        line_number += 1

    full_list.append(firm_dict)
    average_dict[average_name] = round(average_profit / (count - 1))
    full_list.append(average_dict)

with open("txt_files/exercise_7/program_out.json", 'w', encoding='utf8') as file:
    json.dump(full_list, file, ensure_ascii=False)
