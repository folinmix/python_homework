""" Exercise 5
        Реализовать формирование списка, используя функцию range() и возможности генератора.
        В список должны войти четные числа от 100 до 1000 (включая границы).
        Необходимо получить результат вычисления произведения всех элементов списка.

        Подсказка: использовать функцию reduce().
"""
from functools import reduce

my_list = [i for i in range(100, 1000 + 1) if i % 2 == 0]
result = reduce(lambda x, y: x + y, my_list)

print(f"List = {my_list}")
print(f"Sum result = {result}")

