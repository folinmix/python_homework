""" Exercise 2
        Представлен список чисел. Необходимо вывести элементы исходного списка,
        значения которых больше предыдущего элемента.

        Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
        Для формирования списка использовать генератор.
        Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
        Результат: [12, 44, 4, 10, 78, 123].
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

result = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]

print(result)
