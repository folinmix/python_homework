""" Exercise 6
    Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
    Каждый кортеж хранит информацию об отдельном товаре.
    В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
    название, цена, количество, единица измерения).
    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
    Пример готовой структуры:
        [
        (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
        (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
        (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
        ]
    Необходимо собрать аналитику о товарах.
    Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
    а значение — список значений-характеристик, например список названий товаров.
    Пример:
        {
        “название”: [“компьютер”, “принтер”, “сканер”],
        “цена”: [20000, 6000, 2000],
        “количество”: [5, 2, 7],
        “ед”: [“шт.”]
        }
    ПРИМЕЧАНИЕ: не совсем очевидная вещь, однако в словаре (статистика) из примера выше в списках
    только уникальные значения. Для отображения всех значений и уникальных используйте переменную "need_unique"
    Пример:
        need_unique = True  # Только уникальные
        need_unique = False # Все
"""
print("---------------------------Start of program---------------------------")

# Input data by user, define variables
input_message = "Введите информацию о товаре через пробел в следующем формате: "
input_message += "'название' 'цена' 'количество' 'единицы'\n"
name_key = "название"
name_value = ""
price_key = "цена"
price_value = 0
quantity_key = "количество"
quantity_value = 0
units_key = "единицы"
units_value = ""
products = 0
full_quantity = 10
products_list = []
list_to_dict = [[name_key, "word"], [price_key, 1], [quantity_key, 1], [units_key, "word"]]
user_list = []
input_info = 4
check_price = False
check_quantity = False
dict_value_names = []
dict_value_prices = []
dict_value_quantity = []
dict_value_units = []
statistic_dict = {}
need_unique = True

message = f"Введите общее количество позиций товаров (положительное целое число) до {full_quantity} позиций:\n"
while True:
    products = input(message)
    if products.isdigit():
        products = int(products)
        if (products > 0) & (products <= full_quantity):
            break
        else:
            print(f"Ошибка! Нужно целое число из диапазона от 1 до {full_quantity}!")
    else:
        print("Ошибка! Нужно целое число!")

# Generate product structure
for i in range(0, products):
    while True:
        user_list = input(input_message).split(" ")

        if len(user_list) != input_info:
            print("Ошибка! Введённая информация не соответствует ожидаемой!")
        else:
            check_price = user_list[1].isdigit()
            check_quantity = user_list[2].isdigit()
            if check_price & check_quantity:
                list_to_dict[0][1] = user_list[0][:]
                list_to_dict[1][1] = int(user_list[1][:])
                list_to_dict[2][1] = int(user_list[2][:])
                list_to_dict[3][1] = user_list[3][:]
                products_list.append(tuple([i + 1, dict(list_to_dict)]))
                break
            else:
                if not check_price:
                    print("Ошибка! Цена должна быть выражена в цифрах!")
                if not check_quantity:
                    print("Ошибка! Количество должно быть выражено в цифрах!")

# Display generated product structure
print("\nСгенерированная структура (список):")
print("[")
for element in products_list:
    print(element)
print("]")

# Generate dict of products
for element in products_list:
    dict_value_names.append(element[1][name_key])
    dict_value_prices.append(element[1][price_key])
    dict_value_quantity.append(element[1][quantity_key])
    dict_value_units.append(element[1][units_key])

if need_unique:
    dict_value_names = list(set(dict_value_names))
    dict_value_prices = list(set(dict_value_prices))
    dict_value_quantity = list(set(dict_value_quantity))
    dict_value_units = list(set(dict_value_units))

statistic_dict[name_key] = dict_value_names
statistic_dict[price_key] = dict_value_prices
statistic_dict[quantity_key] = dict_value_quantity
statistic_dict[units_key] = dict_value_units

# Display generated product dictionary
print("\nСгенерированный словарь для статистики:")
print("{")
for key, value in statistic_dict.items():
    print(f"'{key}': {value}")
print("}")

print("---------------------------End of program---------------------------")
