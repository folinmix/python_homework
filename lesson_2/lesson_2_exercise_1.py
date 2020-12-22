""" Exercise 1
    Создать список и заполнить его элементами различных типов данных.
    Реализовать скрипт проверки типа данных каждого элемента.
    Использовать функцию type() для проверки типа.
    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
print("---------------------------Start of program---------------------------")

# Define list for some elements with different types and other variables
my_list = [1, 2.0, "Word", ["some_list"], True, {"dict_key": "dict_value"}, ("some_tuple", 10)]
element_count = 1
message = ""

# Display type of each element in list with loop
for element in my_list:
    message = "Type of {number} element is {type}".format(number=element_count, type=type(element).__name__)
    print(message)
    element_count += 1

print("---------------------------End of program---------------------------")
