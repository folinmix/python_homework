""" Exercise 2
    Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
    имя, фамилия, год рождения, город проживания, email, телефон.
    Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.
"""


# Define variables and display_user_data function
write_dict = {"name": "имя",
              "birth": "год рождения",
              "surname": "фамилию",
              "city": "город",
              "email": "электронную почту",
              "phone": "телефон"}


def dict_write(data_dict: dict) -> dict:
    """
        В функцию передаётся словарь, в котором ключи являются заголовками данных пользователя.
        Функция перебирает словарь и предлагает пользователю ввести значения для каждого заголовка данных и
        пытается перевести введённые данные в тип данных, указанный в значении ключа.
        После работы функции в программу возвращается новый словарь.
        :param data_dict: dict
        :return: dict
    """
    user_dict = {}
    message_part_1 = "Пожалуйста, введите "
    message_part_2 = "\n"
    for key, value in data_dict.items():
        message = message_part_1 + value + message_part_2
        data = input(message)
        user_dict[key] = data
    return user_dict


def display_user_data(name: str, surname: str, birth: str, city: str, email: str, phone: str):
    """
        Функция предназначена для вывода информации о пользователе в следующем формате:
        'имя', 'фамилия', 'год рождения', 'город', 'электронная почта', 'телефон'
        :param name: str
        :param surname: str
        :param birth: str
        :param city: str
        :param email: str
        :param phone: str
        :return: None
    """
    message = name + ", " + surname + ", " + birth + ", " + city + ", " + email + ", " + phone
    print(message)


print("---------------------------Start of program---------------------------")

# Work state
user_data_dict = dict_write(write_dict)
display_user_data(**user_data_dict)

print("---------------------------End of program---------------------------")
