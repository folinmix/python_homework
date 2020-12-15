""" Exercise 6
    Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

    Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
    Каждое слово состоит из латинских букв в нижнем регистре.
    Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
    Необходимо использовать написанную ранее функцию int_func().
"""


# Define functions
def int_func(text: str) -> str:
    """
        Функция предназначена для преобразования регистра (из нижнего в верхний) слова
        :param text: str
        :return: str
    """
    data = text[0].upper()
    if len(text) > 1:
        data += text[1:]
    return data


def my_input() -> str:
    """
        Функция предназначена для ввода данных пользователем
        :return: str
    """
    data = input("Введите слово или фразу, разделёную пробелами:\n").split()
    message = ""
    count = False
    for element in data:
        if not count:
            prefix = ""
            count = True
        else:
            prefix = " "
        message += (prefix + int_func(element))
    return message


print("---------------------------Start of program---------------------------")

# Work state
print(my_input())

print("---------------------------End of program---------------------------")
