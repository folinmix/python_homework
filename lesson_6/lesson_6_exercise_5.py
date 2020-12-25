""" Exercise 5
        Реализовать класс Stationery (канцелярская принадлежность).
        Определить в нем атрибут title (название) и метод draw (отрисовка).
        Метод выводит сообщение “Запуск отрисовки.”
        Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
        В каждом из классов реализовать переопределение метода draw.
        Для каждого из классов методы должен выводить уникальное сообщение.
        Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title: str):
        self.title = title

    def drow(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def drow(self):
        return f"Запуск отрисовки с помошью инструмента '{self.title}'."


class Pencil(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def drow(self):
        return f"Запуск отрисовки с помошью инструмента '{self.title}'."


class Handler(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def drow(self):
        return f"Запуск отрисовки с помошью инструмента '{self.title}'."


my_lastik = Stationery("Ластик")
my_pen = Pen("Ручка")
my_pencil = Pencil("Карандаш")
my_handler = Handler("Маркер")

print(my_lastik.drow())
print(my_pen.drow())
print(my_pencil.drow())
print(my_handler.drow())
