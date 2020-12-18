""" Exercise 2
    Для списка реализовать обмен значений соседних элементов,
    т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
    При нечетном количестве элементов последний сохранить на своем месте.
    Для заполнения списка элементов необходимо использовать функцию input().
"""
print("---------------------------Start of program---------------------------")

# Input list elements and define variables, check input symbols is numbers
message = "Введите элементы списка через пробел:\n"
error_message = "Ошибка! Необходимо ввести целые числа!\n"
symbols_digit = True
list_length = 0
help_replace = 0

""" Описание цикла:
    1. Запрос списка чисел у пользователя
        1.1 Запрос списка в первый раз (с использованием только переменной message)
        1.2 Запрос списка повторно, если был введён список с другими символами (error_message + message)
    2. Цикл по введённому списку с проверкой символов на цифры через and (&)
    3. Выход из цикла, если все элемента списка - цифры
"""
while True:
    if symbols_digit:
        my_list = input(message).split(" ")
    else:
        my_list = input(error_message + message).split(" ")
        symbols_digit = True
    for element in my_list:
        symbols_digit = symbols_digit & element.isdigit()
    if symbols_digit:
        break

# Work state (pair replacing)
list_length = len(my_list)
if list_length % 2 != 0:
    list_length -= 2
else:
    list_length -= 1

for i in range(0, list_length, 2):
    help_replace = my_list[i]
    my_list[i] = my_list[i + 1]
    my_list[i + 1] = help_replace

print("Результат попарного обмена элементов в списке:")
print(my_list)

print("---------------------------End of program---------------------------")
