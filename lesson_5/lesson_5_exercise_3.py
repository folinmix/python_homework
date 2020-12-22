""" Exercise 3
        Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
        Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
        Выполнить подсчет средней величины дохода сотрудников.
"""

count = 1
count_min_salary = 1
salary = 0
min_salary = 20000
message = f"Получают менее {min_salary}:\n"
first_min = False

file = open('txt_files/exercise_3/program_in.txt', 'r', encoding='utf-8')
for line in file.readlines():
    if not line:
        continue
    else:
        data = line.split()
        if len(data) != 2:
            print(f"Ошибка! Неверно введены параметры Фамилия - Оклад в {count} строке файла!")
        else:
            try:
                if int(data[1]) < min_salary:
                    if not first_min:
                        print(message + f"{count_min_salary}) {data[0]}")
                        first_min = True
                    else:
                        print(f"{count_min_salary}) {data[0]}")
                    count_min_salary += 1
                count += 1
                salary += int(data[1])
            except ValueError:
                print(f"Ошибка! В параметре Оклад в {count} строке файла введены недопустимые символы!")
file.close()
print(f"При подсчёте по {count - 1} сотрудникам, средний оклад составил {round(salary / (count - 1), 2)}")
