""" Exercise 4
    Программа принимает действительное положительное число x и целое отрицательное число y.
    Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

    Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


# Define functions and variables
my_dict = {"число (положительное значение) в формате float": [float, "pos", "x", "float"],
           "показатель степени (отрицательное значение) в формате int": [int, "neg", "y", "int"]}


def my_power(x: float, y: int) -> float:
    """
        Функция предназначена для возведения числа x в степень y при помощи **
        :param x: float
        :param y: int
        :return: float
    """
    result = x ** y
    return result


def my_power_loop(x: float, y: int) -> float:
    """
        Функция предназначена для возведения числа x в степень y при помощи цикла
        :param x: float
        :param y: int
        :return: float
    """
    result = x
    count = 1
    while count < abs(y):
        result = result * x
        count += 1
    result = 1 / result
    return result


def my_input(data: dict) -> dict:
    """
        Функция предназначена для ввода числа, возводимого в степень (x), и показателя степени (y)
        :param data: dict
        :return: list
    """
    result = {}
    for key, value in data.items():
        while True:
            user_data = input("Введите " + key + ":\n")
            try:
                variable = value[0](user_data)
                if value[1] == "pos":
                    if variable > 0:
                        result[value[2]] = variable
                        break
                    else:
                        print("Ошибка! Число должно быть положительным!\n")
                else:
                    if variable < 0:
                        result[value[2]] = variable
                        break
                    else:
                        print("Ошибка! Число должно быть отрицательным!\n")
            except ValueError:
                print("Ошибка! Тип данных должен быть" + value[3] + "!\n")
    return result


print("---------------------------Start of program---------------------------")

# Work state
user_numbers = my_input(my_dict)
print("Результат возведения в степень при помощи **     :" + str(my_power(**user_numbers)))
print("Результат возведения в степень при помощи цикла  :" + str(my_power_loop(**user_numbers)))

print("---------------------------End of program---------------------------")
