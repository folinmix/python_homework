""" Exercise 5
    Программа запрашивает у пользователя строку чисел, разделенных пробелом.
    При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
    разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
    уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
    Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
    полученной ранее сумме и после этого завершить программу.
"""


# Define functions
def my_input(invitation: str) -> dict:
    """
        Функция предназначена для получения массива при вводе пользователем чисел для суммирования
        :param invitation: str
        :return: dict
    """
    data_array = input(invitation).split()
    result = {"end": False}
    numbers = []
    for element in data_array:
        try:
            numbers.append(int(element))
        except ValueError:
            if element == "/":
                result["end"] = True
                break
            else:
                print("Ошибка! Введены недопустимые символы!")
    result["numbers"] = numbers
    return result


def my_sum():
    """
        Фукция предназначена для получения суммы введённых чисел.
    """
    message = "Введите числа в формате int через пробел для вычисления суммы. Для завершения введите '/'\n"
    end_sum = 0
    while True:
        data = my_input(message)
        end_sum += sum(data["numbers"])
        print("Текущая сумма = " + str(end_sum))
        if data["end"]:
            break


print("---------------------------Start of program---------------------------")

# Work state
my_sum()

print("---------------------------End of program---------------------------")
