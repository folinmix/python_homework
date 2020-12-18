""" Exercise 4
        Представлен список чисел. Определить элементы списка, не имеющие повторений.
        Сформировать итоговый массив чисел, соответствующих требованию.
        Элементы вывести в порядке их следования в исходном списке.
        Для выполнения задания обязательно использовать генератор.

        Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
        Результат: [23, 1, 3, 10, 4, 11]
"""

while True:
    my_list = input("Введите числа списка через пробел:\n").split()
    count = 0
    flag = True
    for i in range(0, len(my_list)):
        try:
            my_list[i] = int(my_list[i])
        except ValueError:
            print("Ошибка! Введены недопустимые символы!")
            flag = False
            break
    if flag:
        break


result = [element for element in my_list if my_list.count(element) == 1]
print(result)
