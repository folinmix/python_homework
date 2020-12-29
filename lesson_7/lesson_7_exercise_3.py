""" Exercise 3
        Реализовать программу работы с органическими клетками.
        Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
        количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических
        операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
        Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
        (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление
        значения до целого числа.

        Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
            исходных двух клеток.
        Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества
            ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
        Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
            количества ячеек этих двух клеток.
        Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
            деление количества ячеек этих двух клеток.

        В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
        Данный метод позволяет организовать ячейки по рядам.

        Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
        переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
        все оставшиеся.

        Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
        Тогда метод make_order() вернет строку: *****\n*****\n**.

        Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
        Тогда метод make_order() вернет строку: *****\n*****\n*****.

        Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:

    def __init__(self, quantity: int):
        self.message = ""
        try:
            self.quantity = int(quantity)
        except ValueError:
            exit("Ошибка! Количетсво клеток должно быть целым числом!")

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        self.message = "Невозможно вычесть!"
        return Cell(self.quantity - other.quantity) if self.quantity > other.quantity else self.message

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        try:
            return Cell(int(self.quantity / other.quantity))
        except ZeroDivisionError:
            print("Нельзя делить на нуль!")

    def make_order(self, line_quantity):
        result = '\n'.join([line_quantity * '*' for _ in range(self.quantity // line_quantity) \
                            if self.quantity > line_quantity])
        prefix = '\n' if self.quantity > line_quantity else ''
        return result + prefix + (self.quantity % line_quantity) * '*'


cell_1 = Cell(10)
cell_2 = Cell(2)

add_cell = cell_1 + cell_2
print(f'add_cell =  {add_cell.quantity}')
sub_cell_1 = cell_1 - cell_2
print(f'sub_cell_1 =  {sub_cell_1.quantity}')
sub_cell_2 = cell_2 - cell_1
print(f'sub_cell_2 =  {sub_cell_2.quantity if type(sub_cell_2) == "Class" else "Невозможно вычесть!"}')
mul_cell = cell_1 * cell_2
print(f'mul_cell =  {mul_cell.quantity}')
div_cell = cell_1 / cell_2
print(f'div_cell =  {div_cell.quantity}')

cell_3 = Cell(29)
print(cell_3.make_order(9))
