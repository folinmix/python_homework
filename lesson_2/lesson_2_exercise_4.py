""" Exercise 4
    Пользователь вводит строку из нескольких слов, разделённых пробелами.
    Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
    Если в слово длинное, выводить только первые 10 букв в слове.
"""
print("---------------------------Start of program---------------------------")

# Input string data by user and define variables
max_symbols = 10
line_count = 1
message = ""
user_data = input("Введите текст, разделяя слова пробелами\n").split(" ")

# Work state. Get elements from list and display it
for element in user_data:
    if len(element) > max_symbols:
        element = element[0:max_symbols]
    message = f"{line_count}-ая строка) {element}"
    print(message)
    line_count += 1

print("---------------------------End of program---------------------------")
