""" Exercise_1
        Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
        Об окончании ввода данных свидетельствует пустая строка.
"""

file = open('txt_files/exercise_1/program_out.txt', 'w', encoding='UTF-8')
while True:
    data_user = input("Введите строку для записи в файл. Для завершения оставьте строку пустой:\n")
    if not data_user:
        break
    else:
        file.writelines(data_user + '\n')
file.close()
