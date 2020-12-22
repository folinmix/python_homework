""" Exercise 4
        Создать (не программно) текстовый файл со следующим содержимым:
            One — 1
            Two — 2
            Three — 3
            Four — 4
        Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
        При этом английские числительные должны заменяться на русские.
        Новый блок строк должен записываться в новый текстовый файл.
"""

my_dict = {"one": "Один",
           "two": "Два",
           "three": "Три",
           "four": "Четыре",
           "five": "Пять",
           "six": "Шесть",
           "seven": "Семь",
           "eight": "Восемь",
           "nine": "Девять"}

file = open('txt_files/exercise_4/program_in.txt', 'r', encoding='UTF-8')
data = file.readlines()
file.close()

file = open('txt_files/exercise_4/program_out.txt', 'w', encoding='UTF-8')
for line in data:
    my_list = line.split()
    file.write(my_dict[my_list[0].lower()] + ' ' + ' '.join(my_list[1:]) + '\n')
file.close()
