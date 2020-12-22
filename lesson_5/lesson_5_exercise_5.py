""" Exercise 5
        Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
        Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

while True:
    user_data = input("Введите числа в формате int через пробел:\n").split()
    buf_variable = 0
    if not user_data:
        print("Ошибка! Отсутствие данных!")
    else:
        try:
            for el in user_data:
                buf_variable = int(el)
            break
        except ValueError:
            print("Ошибка! Введены недопустимые символы!")

with open('txt_files/exercise_5/program_out.txt', 'w', encoding='UTF-8') as file:
    file.write(' '.join(user_data))

numbers_sum = 0
count = 0
with open('txt_files/exercise_5/program_out.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    for el in data.split():
        numbers_sum += int(el)
        count += 1
print(f"Сумма {count} чисел из файла равна {numbers_sum}")
