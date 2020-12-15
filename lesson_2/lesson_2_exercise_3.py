""" Exercise 3
    Пользователь вводит месяц в виде целого числа от 1 до 12.
    Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
    Напишите решения через list и через dict.
"""
print("---------------------------Start of program---------------------------")

# Input int in range 1 to 12 by user (and check it), define variables
message_list = ""
message_dict = ""
list_season = ""
dict_season = ""
compare_list = ["зима",
                "зима",
                "весна",
                "весна",
                "весна",
                "лето",
                "лето",
                "лето",
                "осень",
                "осень",
                "осень",
                "зима"]
compare_dict = {1: "зима",
                2: "зима",
                3: "весна",
                4: "весна",
                5: "весна",
                6: "лето",
                7: "лето",
                8: "лето",
                9: "осень",
                10: "осень",
                11: "осень",
                12: "зима"}

""" Описание цикла:
    1. Запрос номера месяца у пользователя
    2. Проверка, что введённое значение - число в формате int
        2.1 Проверка, что значение в диапазоне от 1 до 12
            2.1.1 В диапазоне - выход из цикла
            2.1.2 Вне диапазона - вывод сообщения об ошибке (вне диапазона)
        2.2 Вывод сообщения об ошибке (введены не только цифры)
"""
while True:
    month_number = input("Введите номер месяца от 1 до 12:\n")
    if month_number.isdigit():
        month_number = int(month_number)
        if (month_number > 0) & (month_number <= 12):
            break
        else:
            print("Ошибка! Номер должен быть больше 0 и меньше 12!")
    else:
        print("Ошибка! Нужно вводить только цифры!")

# Work state. Get values from list and dict
list_season = compare_list[month_number - 1]
dict_season = compare_dict[month_number]
message_list = "По списку, {number}-й месяц - это {season}".format(number=month_number, season=list_season)
message_dict = "По словарю, {number}-й месяц - это {season}".format(number=month_number, season=dict_season)
print(message_list)
print(message_dict)

print("---------------------------End of program---------------------------")
