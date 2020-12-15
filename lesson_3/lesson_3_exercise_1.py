""" Exercise 1
    Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


# Define 2 functions - division function and input function
def my_division() -> str:
    """
        Функия предназначена для деления с округлением двух чисел.
        Для ввода чисел в функцию используется другая функция.
        В случае, если делитель равен нулю, выдаётся
        сообщение о том, что на нуль деление в данной программе не предусмотрено.
        :return: str
    """
    message_1 = "Введите первое число:\n"
    message_2 = "Введите второе число:\n"
    number_1 = my_input(message_1)
    number_2 = my_input(message_2)
    try:
        result = "Результат деления:" + str(round((number_1 / number_2), 2))
    except ZeroDivisionError:
        result = "Деление на нуль не допускается!\n"
    return result


def my_input(message: str) -> float:
    """
        Функия предназначена для ввода числа с клавиатуры.
        После ввода осуществляется перевод типа введённого числа str -> float.
        Если преобразование небозможно, функция продолжает работу до правильного ввода c
        выводом сообщения об ошибке.
        :param message: str
        :return: float
    """
    while True:
        try:
            number = float(input(message))
            break
        except ValueError:
            print("Ошибка! Необходимо ввести число в формате int или float!\n")
    return number


print("---------------------------Start of program---------------------------")

# Work state
print(my_division())

print("---------------------------End of program---------------------------")
