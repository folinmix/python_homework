""" Exercise 3
    Реализовать функцию my_func(), которая принимает три позиционных аргумента
    и возвращает сумму наибольших двух аргументов.
"""


# Define functions and variables
def my_input() -> list:
    """
        Функия предназначена для ввода чисел с клавиатуры.
        После ввода осуществляется перевод типа введённого числа str -> int.
        Если преобразование небозможно, функция продолжает работу до правильного ввода c
        выводом сообщения об ошибке.
        :return: list
    """
    data_count = 1
    max_count = 3
    numbers = []
    while data_count <= max_count:
        message = "Введите " + str(data_count) + " число:\n"
        while True:
            try:
                numbers.append(int(input(message)))
                data_count += 1
                break
            except ValueError:
                print("Ошибка! Необходимо ввести число в формате int!\n")
    return numbers


def my_func(*numbers: int) -> int:
    """
        Функия предназначена для сложения двух наибольших чисел из трёх введённых.
        :param numbers: int
        :return: int
    """
    result = my_max(*numbers)
    numbers_sum = sum(result)
    return numbers_sum


def my_max(*numbers: int) -> list:
    """
        Функия предназначена для сортировки данных от большего к меньшему из исхоодного массива.
        :param numbers: int
        :return: list
    """
    result = []
    if numbers[0] > numbers[1]:
        max_first = numbers[0]
        max_second = numbers[1]
    else:
        max_first = numbers[1]
        max_second = numbers[0]
    if numbers[2] > max_first:
        max_second = max_first
        max_first = numbers[2]
    else:
        if numbers[2] > max_second:
            max_second = numbers[2]
    result.append(max_first)
    result.append(max_second)
    return result


print("---------------------------Start of program---------------------------")

# Work state
my_list = my_input()
sum_result = my_func(*my_list)
print("Результат суммы равен:" + str(sum_result))

print("---------------------------End of program---------------------------")
