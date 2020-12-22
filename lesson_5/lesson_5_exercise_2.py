""" Exercise 2
        Создать текстовый файл (не программно), сохранить в нем несколько строк,
        выполнить подсчет количества строк, количества слов в каждой строке.
"""

count = 1

file = open('txt_files/exercise_2/program_in.txt', 'r', encoding='utf-8')
for line in file.readlines():
    print(f"В {count} строке {len(line.split())} слов")
    count += 1
file.close()
